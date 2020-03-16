import re
from functools import lru_cache
from typing import List, Tuple, Union, Match

from restit.internal.request_body_properties import RequestBodyProperties
from restit.internal.response_status_parameter import ResponseStatusParameter
from restit.open_api.info_object import InfoObject
from restit.open_api.open_api_schema_converter import \
    OpenApiSchemaConverter
from restit.resource import PathParameter
from restit.resource import Resource


class OpenApiDocumentation:
    _IGNORE_RESOURCE_CLASS_NAMES = ["DefaultFaviconResource", "OpenApiResource"]
    _SPEC_VERSION = "3.0.0"

    def __init__(self, info: InfoObject, path: str = "/api"):
        self.info = info
        self.path = path
        self._resources: List[Resource] = []
        self._servers = []

    def register_resource(self, resource: Resource):
        if resource not in self._resources and \
                resource.__class__.__name__ not in OpenApiDocumentation._IGNORE_RESOURCE_CLASS_NAMES:
            self._resources.append(resource)

    @lru_cache(maxsize=1)
    def generate_spec(self) -> dict:
        self._resources.sort(key=lambda r: r.__request_mapping__)
        spec_structure = self._generate_base_spec_structure()
        self._generate_paths(spec_structure)
        return spec_structure

    def _generate_paths(self, spec_structure):
        paths = spec_structure["paths"]
        for resource in self._resources:
            if resource.__request_mapping__:
                self._add_resource(paths, resource, spec_structure)

    def _add_resource(self, paths: dict, resource: Resource, spec_structure: dict):
        path, inferred_path_parameters = \
            self._infer_path_params_and_open_api_path_syntax(resource.__request_mapping__)
        paths[path] = {}
        for method_name, method_object in self._get_allowed_resource_methods(resource).items():
            paths[path][method_name] = {
                "responses": {},
                "parameters": []
            }

            method_spec = paths[path][method_name]
            self._add_summary_and_description_to_method(method_spec, method_object)
            self._add_path_parameters(method_spec, resource, inferred_path_parameters)
            self._add_query_parameters(method_spec, method_object)
            self._add_request_body(method_spec, method_object, spec_structure)
            self._add_responses(method_spec, method_object, spec_structure)

    @staticmethod
    def _add_responses(method_spec: dict, method_object: object, spec_structure: dict):
        response_status_parameters = getattr(method_object, "__response_status_parameters__", None)
        if response_status_parameters:
            for response_status_parameter in response_status_parameters:  # type: ResponseStatusParameter
                method_spec["responses"][response_status_parameter.status or "default"] = {
                    "description": response_status_parameter.description,
                    "content": OpenApiDocumentation._create_content_field(response_status_parameter.content_types)
                }

    @staticmethod
    def _add_request_body(method_spec: dict, method_object: object, spec_structure: dict):
        request_body_parameter = getattr(
            method_object, "__request_body_properties__", None)  # type: RequestBodyProperties
        if request_body_parameter:
            # ToDo allow creating global schema under components
            # spec_structure["components"]["schemas"][request_body_parameter.schema.__class__.__name__] = \
            #    MarshmallowToOpenApiSchemaConverter.convert(request_body_parameter.schema)

            method_spec["requestBody"] = {
                "description": request_body_parameter.description,
                "required": request_body_parameter.required,
                "content": OpenApiDocumentation._create_content_field(request_body_parameter.content_types)
            }

    @staticmethod
    def _create_content_field(content_types: dict):
        return {
            content_type:
                {
                    "schema": OpenApiSchemaConverter.convert(schema)
                }
            for content_type, schema in content_types.items()
        }

    @staticmethod
    def _add_query_parameters(method_spec: dict, method_object: object):
        method_spec["parameters"].extend([
            {
                "name": query_parameter.name,
                "in": "query",
                "description": query_parameter.description,
                "required": query_parameter.field_type.required,
                "schema": OpenApiSchemaConverter.convert(query_parameter.field_type)
            }
            for query_parameter in getattr(method_object, "__query_parameters__", [])
        ])

    @staticmethod
    def _add_path_parameters(method_spec: dict, resource: Resource, inferred_path_parameters: List[PathParameter]):
        parameter_definitions = getattr(resource, "__path_parameters__", [])
        path_parameters = {
            path_parameter.name: path_parameter for path_parameter in inferred_path_parameters
        }
        path_parameters.update({
            path_parameter.name: path_parameter for path_parameter in parameter_definitions
        })

        method_spec["parameters"].extend([
            {
                "name": name,
                "in": "path",
                "required": True,
                "description": path_parameter.description,
                "schema": OpenApiSchemaConverter.convert_field(path_parameter.field_type)

            } for name, path_parameter in path_parameters.items()
        ])

    @staticmethod
    def _infer_path_params_and_open_api_path_syntax(path: str) -> Tuple[str, List[PathParameter]]:
        path_parameter_list = []

        def _handle_path_parameter(match: Match) -> str:
            path_parameter_list.append(
                PathParameter(match.group(1), "", eval(match.group(2)) if match.group(2) else str)
            )
            return "{%s}" % match.group(1)

        openapi_path_syntax = re.sub(r":(\w+)(?:<(\w+)>)?", _handle_path_parameter, path)
        return openapi_path_syntax, path_parameter_list

    def _add_summary_and_description_to_method(self, method_spec: dict, method_object: object):
        summary, description = self._get_summary_and_description_from_doc(method_object.__doc__)
        method_spec["summary"] = summary
        method_spec["description"] = description

    @staticmethod
    def _get_summary_and_description_from_doc(doc: str) -> Tuple[Union[str, None], Union[str, None]]:
        if not doc:
            return None, None

        doc_split = doc.split("\n")
        summary = doc_split[0]
        description = "\n".join(doc_split[1:]) if len(doc) > 1 else None
        return summary.strip("\n "), description.strip("\n ")

    @staticmethod
    def _get_allowed_resource_methods(resource: Resource) -> dict:
        allowed_methods_dict = {allowed: getattr(resource, allowed) for allowed in resource.get_allowed_methods()}
        return allowed_methods_dict

    def _generate_base_spec_structure(self) -> dict:
        return {
            "openapi": OpenApiDocumentation._SPEC_VERSION,
            "info": self.info.to_dict(),
            "paths": {},
            "components": {
                "schemas": {}
            }
        }
