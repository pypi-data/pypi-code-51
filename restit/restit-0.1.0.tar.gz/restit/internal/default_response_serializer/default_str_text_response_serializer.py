from typing import List, Tuple, Union

from restit.common import get_default_encoding, guess_text_content_subtype_string
from restit.internal.response_status_parameter import ResponseStatusParameter
from restit.response_serializer import ResponseSerializer


class DefaultStrTextResponseSerializer(ResponseSerializer):
    def get_media_type_strings(self) -> List[str]:
        return ["text/plain"]

    def get_response_data_type(self) -> type:
        return str

    def validate_and_serialize(
            self, response_input: str, response_status_parameter: Union[None, ResponseStatusParameter]
    ) -> Tuple[bytes, str]:
        content_type = guess_text_content_subtype_string(response_input)
        if self.find_schema(content_type, response_status_parameter):
            raise DefaultStrTextResponseSerializer.SchemaNotSupportedForStringResponseBody()

        return response_input.encode(encoding=get_default_encoding()), content_type

    class SchemaNotSupportedForStringResponseBody(Exception):
        pass
