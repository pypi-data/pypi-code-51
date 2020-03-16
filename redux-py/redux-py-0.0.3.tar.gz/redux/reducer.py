"""
    Implements reducer related function
"""

from typing import Dict, Mapping, Optional

from .action import select_action_type
from .types import Action, PayloadType, Reducer, StateType


def default_reducer(initial_state: Optional[StateType]) -> Reducer:
    """ Creates a reducer that returns the original state or the default state. 

        Args:
            inital_state: optional initial state used as a fallback

        Returns:
            A reducer that reduces the current state or the initial state as a fallback
    
    """

    def reducer(state: StateType, action: Action) -> Optional[StateType]:
        """ Reducer that returns the state or the initial state

            Args:
                state: the current state
                action: the action, will be ignored by the function

            Returns:
                The state of the initial state as a fallback
        
        """
        return state if state else initial_state

    return reducer


def handle_actions(
    action_map: Mapping[str, Reducer[StateType, PayloadType]],
    initial_state: Optional[StateType] = None,
) -> Reducer[StateType, PayloadType]:

    """ Creates a new reducer from a mapping of action name to reducer for that action. 

        Args:
            action_map: mapping from action name to reducer for that action
            initial_state: optional initial state used if no reducer matches

        Returns:
            A reducer function that handles the actions in the map
    
    """
    def_reducer = default_reducer(initial_state)

    def reducer(state: StateType, action: Action) -> Optional[StateType]:
        """ Applies the mapped reducer or returns the default state

            Args:
                state: current state
                action: action to apply against the current state

            Returns:
                the updated state 
        """
        return action_map.get(select_action_type(action), def_reducer)(state, action)

    return reducer


def combine_reducers(reducers: Mapping[str, Reducer]) -> Reducer:
    """ Creates a new reducer from a mapping of reducers. 

        Args: 
            reducers: the mapping from state partition to reducer
        
        Returns:
            A reducer that dispatches actions against each of the mapped reducers
    
    """
    items = reducers.items()

    def combine(state: Dict[str, StateType], action: Action) -> Mapping[str, StateType]:
        """ Updates the state object from the reducer mappings. """
        result = state
        for key, value in items:
            current = state.get(key)
            updated = value(current, action)
            if not current is updated:
                if result is state:
                    result = dict(state)
                result[key] = updated
        return result

    return combine
