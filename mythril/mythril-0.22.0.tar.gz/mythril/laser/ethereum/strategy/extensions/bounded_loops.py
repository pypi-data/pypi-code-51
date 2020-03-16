from mythril.laser.ethereum.state.global_state import GlobalState
from mythril.laser.ethereum.strategy.basic import BasicSearchStrategy
from mythril.laser.ethereum.state.annotation import StateAnnotation
from mythril.laser.ethereum.transaction import ContractCreationTransaction
from typing import Dict, cast, List
from copy import copy
import logging


log = logging.getLogger(__name__)


class JumpdestCountAnnotation(StateAnnotation):
    """State annotation that counts the number of jumps per destination."""

    def __init__(self) -> None:
        self._reached_count = {}  # type: Dict[int, int]
        self.trace = []  # type: List[int]

    def __copy__(self):
        result = JumpdestCountAnnotation()
        result._reached_count = copy(self._reached_count)
        result.trace = copy(self.trace)
        return result


class BoundedLoopsStrategy(BasicSearchStrategy):
    """Adds loop pruning to the search strategy.
    Ignores JUMPI instruction if the destination was targeted >JUMPDEST_LIMIT times.
    """

    def __init__(self, super_strategy: BasicSearchStrategy, *args) -> None:
        """"""

        self.super_strategy = super_strategy
        self.bound = args[0][0]

        log.info(
            "Loaded search strategy extension: Loop bounds (limit = {})".format(
                self.bound
            )
        )

        BasicSearchStrategy.__init__(
            self, super_strategy.work_list, super_strategy.max_depth
        )

    def calculate_hash(self, i, j, trace):
        """
        calculate hash(trace[i: j])
        :param i:
        :param j:
        :param trace:
        :return: hash(trace[i: j])
        """
        key = 0
        size = 0
        for itr in range(i, j):
            key |= trace[itr] << ((itr - i) * 8)
            size += 1

        return key

    def count_key(self, trace, key, start, size):
        """
        Count continuous loops in the trace.
        :param trace:
        :param key:
        :param size:
        :return:
        """
        count = 0
        i = start
        while i >= 0:
            if self.calculate_hash(i, i + size, trace) != key:
                break
            count += 1
            i -= size
        return count

    def get_strategic_global_state(self) -> GlobalState:
        """ Returns the next state

        :return: Global state
        """

        while True:

            state = self.super_strategy.get_strategic_global_state()

            annotations = cast(
                List[JumpdestCountAnnotation],
                list(state.get_annotations(JumpdestCountAnnotation)),
            )

            if len(annotations) == 0:
                annotation = JumpdestCountAnnotation()
                state.annotate(annotation)
            else:
                annotation = annotations[0]

            cur_instr = state.get_current_instruction()

            annotation.trace.append(cur_instr["address"])

            if cur_instr["opcode"].upper() != "JUMPDEST":
                return state

            # create unique instruction identifier

            found = False
            for i in range(len(annotation.trace) - 3, 0, -1):
                if (
                    annotation.trace[i] == annotation.trace[-2]
                    and annotation.trace[i + 1] == annotation.trace[-1]
                ):
                    found = True
                    break

            if found:
                key = self.calculate_hash(
                    i, len(annotation.trace) - 1, annotation.trace
                )
                size = len(annotation.trace) - i - 1
                count = self.count_key(annotation.trace, key, i, size)
            else:
                count = 0

            # The creation transaction gets a higher loop bound to give it a better chance of success.
            # TODO: There's probably a nicer way to do this

            if isinstance(
                state.current_transaction, ContractCreationTransaction
            ) and count < max(8, self.bound):
                return state

            elif count > self.bound:
                log.debug("Loop bound reached, skipping state")
                continue

            return state
