import logging
from collections import namedtuple
from typing import List

from marshmallow.fields import Field, String

LOGGER = logging.getLogger(__name__)

QueryParameter = namedtuple("QueryParameter", ["name", "description", "field_type"])


# noinspection PyShadowingBuiltins
def query_parameter(name: str, description: str, field_type: Field = String):
    def decorator(func):
        _query_parameter = QueryParameter(name, description, field_type)
        registered_query_parameters: List[QueryParameter] = getattr(func, "__query_parameters__", [])
        LOGGER.debug(
            "Registering query parameter %s for %s", _query_parameter, func.__name__
        )
        registered_query_parameters.append(_query_parameter)
        setattr(func, "__query_parameters__", registered_query_parameters)
        return func

    return decorator
