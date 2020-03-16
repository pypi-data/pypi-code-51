import logging
from http import HTTPStatus
from typing import Dict, Union, List

from marshmallow import Schema
from marshmallow.fields import Field

from restit.internal.response_status_parameter import ResponseStatusParameter

LOGGER = logging.getLogger(__name__)


# noinspection PyShadowingBuiltins
def response_status(status: Union[int, HTTPStatus], content_types: Dict[str, Union[Schema, Field]], description: str):
    def decorator(func):
        http_status_code = status if isinstance(status, int) or status is None else status.value
        response_status_parameter = ResponseStatusParameter(http_status_code, description, content_types)

        registered_response_status_parameters: List[ResponseStatusParameter] = \
            getattr(func, "__response_status_parameters__", [])
        LOGGER.debug(
            "Registering response status parameter %s for %s", response_status_parameter, func.__name__
        )
        registered_response_status_parameters.append(response_status_parameter)
        setattr(func, "__response_status_parameters__", registered_response_status_parameters)
        return func

    return decorator
