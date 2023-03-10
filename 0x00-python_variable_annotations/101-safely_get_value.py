#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar("T"), None] = None) -> Union[
        Any, TypeVar("T")]:
    """
    Returns the value associated with the key in the mapping,
    or None as default if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
