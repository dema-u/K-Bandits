from abc import ABC, abstractmethod
from typing import List, Tuple


class Algorithm(ABC):

    @abstractmethod
    def __init__(self, k: int, sampling_method:str='sample', optimistic: bool=False):
        self.arm_info = self._initiate_list(k, optimistic)
        self.sampling = sampling_method

    @abstractmethod
    def action_arm(self) -> int:
        pass

    @abstractmethod
    def learn_arm(self, arm_no: int, reward: float) -> None:
        pass

    def _initiate_list(self, k, optimistic) -> List[Tuple]:
        initial_belief = [(0, 1) for _ in range(k)] if optimistic else [(0, 0) for _ in range(k)]
        return initial_belief