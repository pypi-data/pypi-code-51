import json
from typing import List, Tuple, Union

from restit.common import get_default_encoding
from restit.internal.response_status_parameter import ResponseStatusParameter
from restit.response_serializer import ResponseSerializer


class DefaultDictJsonResponseSerializer(ResponseSerializer):
    def get_media_type_strings(self) -> List[str]:
        return ["application/json", "application/problem+json"]

    def get_response_data_type(self) -> type:
        return dict

    def validate_and_serialize(
            self, response_input: dict, response_status_parameter: Union[None, ResponseStatusParameter]
    ) -> Tuple[bytes, str]:
        content_type = "application/json"
        schema = ResponseSerializer.find_schema(content_type, response_status_parameter)
        if schema:
            json_string = schema.dumps(response_input)
        else:
            json_string = json.dumps(response_input)
        return json_string.encode(encoding=get_default_encoding()), content_type
