from typing import Any, Callable, Dict, Optional

from chalice.app import Chalice, RouteEntry  # noqa
from chalice.deploy.swagger import SwaggerGenerator
from chalice.deploy.models import RestAPI  # noqa

from leangle.leangle import _leangle_schemas

from marshmallow_jsonschema import JSONSchema


original_generate_swagger = SwaggerGenerator.generate_swagger
original_generate_route_method = SwaggerGenerator._generate_route_method


def patch_generate_swagger() -> Callable:
    """Monkey Patch SwaggerGenerator.generate_swagger."""
    def generate_swagger(self,
                         app: Chalice,
                         rest_api: Optional[RestAPI] = None) -> Dict[str, Any]:
        api: Dict[str, Any] = original_generate_swagger(self, app, rest_api)
        _add_leangle_schemas(api)
        return api
    return generate_swagger


def _add_leangle_schemas(api: Dict):
    """Add schema dumps to the API."""
    for schema in _leangle_schemas:
        api['definitions'].update(JSONSchema().dump(schema())['definitions'])
    return api


def patch_generate_route_method() -> Callable:
    """Monkey Patch SwaggerGenerator._generate_route_method."""
    def _generate_route_method(self, view: RouteEntry) -> Dict[str, Any]:
        responses = getattr(
            view.view_function,
            '_leangle_responses',
            self._generate_precanned_responses(),
        )

        parameters = getattr(
            view.view_function,
            '_leangle_parameters',
            [],
        )

        current = original_generate_route_method(self, view)

        current_parameters = current.get('parameters', [])

        current['parameters'] = [*current_parameters, *parameters]
        current['responses'] = responses
        return current

    return _generate_route_method
