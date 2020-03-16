"""Functions for parsing the inheritance for accumulating attributes.

Accumulating attributes are both defined and can be added to and removed from further down the hierarchy.
The hierarchy is also slightly different to the other fields as it is determined as 'breadth-first' in
multiple inheritance, so targets at a lower level will always take precedence over targets at a higher level.
"""
import itertools
from collections import deque
from typing import Dict, List, Any, Deque

ACCUMULATING_ATTRIBUTES = ["extra_labels", "macros", "device_has", "features", "components"]
ALL_ACCUMULATING_ATTRIBUTES = ACCUMULATING_ATTRIBUTES + [
    "extra_labels_remove",
    "extra_labels_add",
    "macros_remove",
    "macros_add",
    "device_has_remove",
    "device_has_add",
    "features_remove",
    "features_add",
    "components_remove",
    "components_add",
]


def get_accumulating_attributes_for_target(all_targets_data: Dict[str, Any], target_name: str) -> Dict[str, Any]:
    """Parses the data for all targets and returns the accumulating attributes for the specified target.

    Args:
        all_targets_data: a dictionary representation of the contents of targets.json
        target_name: the name of the target to find the attributes of

    Returns:
        A dictionary containing all the accumulating attributes for the chosen target
    """
    accumulating_order = _targets_accumulate_hierarchy(all_targets_data, target_name)
    return _determine_accumulated_attributes(accumulating_order)


def _targets_accumulate_hierarchy(all_targets_data: Dict[str, Any], target_name: str) -> List[dict]:
    """List all ancestors of a target in order of accumulation inheritance (breadth-first).

    Using a breadth-first traverse of the inheritance tree, return a list of targets in the
    order of inheritance, starting with the target itself and finishing with its highest ancestor.

    Args:
        all_targets_data: a dictionary representation of all the data in a targets.json file
        target_name: the name of the target we want to calculate the attributes for

    Returns:
        A list of dicts representing each target in the hierarchy.
    """
    accumulation_order: List[dict] = []

    still_to_visit: Deque[dict] = deque()
    still_to_visit.appendleft(all_targets_data[target_name])

    while still_to_visit:
        current_target = still_to_visit.popleft()
        accumulation_order.append(current_target)
        for parent_target in current_target.get("inherits", []):
            still_to_visit.append(all_targets_data[parent_target])

    return accumulation_order


def _add_attribute_element(
    accumulator: Dict[str, Any], attribute_name: str, elements_to_add: List[Any]
) -> Dict[str, Any]:
    """Adds an attribute element to an attribute.

    Args:
        accumulator: a store of attributes to be updated
        attribute_name: name of the attribute to update
        elements_to_add: element to add to the attribute list

    Returns:
        The accumulator object with the new elements added
    """
    for element in elements_to_add:
        accumulator[attribute_name].append(element)
    return accumulator


def _element_matches(element_to_remove: str, element_to_check: str) -> bool:
    """Checks if an element meets the criteria to be removed from list.

    Some attribute elements (eg. macros) can be defined with a number value
    eg. MACRO_SOMETHING=5. If we are then instructed to remove
    MACRO_SOMETHING then this element needs to be recognised and removed
    in addition to exact matches.

    Args:
        element_to_remove: the element as taken from list to be removed from an attribute
        element_to_check: an element that currently makes up part of an attribute definition

    Returns:
        A boolean reflecting whether the element is a match and should be removed
    """
    return element_to_check == element_to_remove or element_to_check.startswith(f"{element_to_remove}=")


def _remove_attribute_element(
    accumulator: Dict[str, Any], attribute_name: str, elements_to_remove: List[Any]
) -> Dict[str, Any]:
    """Removes an attribute element from an attribute.

    Args:
        accumulator: a store of attributes to be updated
        attribute_name: name of the attribute to update
        elements_to_remove: element to remove from the attribute list

    Returns:
        The accumulator object with the desired elements removed
    """
    existing_elements = accumulator[attribute_name]
    combinations_to_check = itertools.product(existing_elements, elements_to_remove)
    checked_elements_to_remove = [
        existing_element
        for existing_element, element in combinations_to_check
        if _element_matches(element, existing_element)
    ]

    for element in checked_elements_to_remove:
        accumulator[attribute_name].remove(element)
    return accumulator


def _calculate_attribute_elements(
    attribute_name: str, starting_state: Dict[str, Any], applicable_accumulation_order: List[dict]
) -> Dict[str, Any]:
    """Adds and removes elements for an attribute based on the definitions encountered in the hierarchy.

    Args:
        attribute_name: name of the attribute to update
        starting_state: the list of elements that defines the starting state of the attribute
        applicable_accumulation_order: the targets in the inheritance tree that can contain add and remove modifiers

    Returns:
        The elements calculated for an attribute according to the target's inheritance
    """
    accumulator = starting_state
    for target in reversed(applicable_accumulation_order):
        if f"{attribute_name}_add" in target.keys():
            to_add = target[f"{attribute_name}_add"]
            _add_attribute_element(accumulator, attribute_name, to_add)
        if f"{attribute_name}_remove" in target.keys():
            to_remove = target[f"{attribute_name}_remove"]
            _remove_attribute_element(accumulator, attribute_name, to_remove)
    return accumulator


def _calculate_attribute_for_target(
    attribute_name: str, target: Dict[str, Any], accumulation_order: List[dict]
) -> Dict[str, Any]:
    """Finds a single accumulated attribute for a target from its list of ancestors.

    Args:
        attribute_name: the name of the accumulating attribute
        target: the target we are collecting data for
        accumulation_order: the full inheritance hierarchy

    Returns:
        A dictionary representation of a single accumulating attribute for that target
    """
    starting_state = {attribute_name: target[attribute_name]}
    # Reduces the order list to only the targets in the hierarchy between the starting state and the target itself
    applicable_accumulation_order = accumulation_order[: accumulation_order.index(target)]
    return _calculate_attribute_elements(attribute_name, starting_state, applicable_accumulation_order)


def _find_nearest_defined_attribute(accumulation_order: List[dict], attribute_name: str) -> Dict[str, Any]:
    """Returns the definition of a particular attribute first encountered in the accumulation order.

    Args:
        accumulation_order: the inheritance order for the target, from the target itself to its highest ancestor
        attribute_name: the attribute to search for

    Returns:
        A dictionary containing the definition of the requested attribute
    """
    for target in accumulation_order:
        if attribute_name in target.keys():
            return _calculate_attribute_for_target(attribute_name, target, accumulation_order)
    return {}


def _determine_accumulated_attributes(accumulation_order: List[dict]) -> Dict[str, Any]:
    """Finds all the accumulated attributes for a target from its list of ancestors.

    Iterates through the order of inheritance (accumulation order) to find the nearest definition
    of an attribute, then retraces backwards calculating additions and deletions that modify it.

    Args:
        accumulation_order: the inheritance order for the target, from the target itself to its highest ancestor

    Returns:
        A dictionary containing all the accumulating attributes for a target
    """
    accumulated_attributes = {}

    for attribute_name in ACCUMULATING_ATTRIBUTES:
        accumulated_attributes.update(_find_nearest_defined_attribute(accumulation_order, attribute_name))
    return accumulated_attributes
