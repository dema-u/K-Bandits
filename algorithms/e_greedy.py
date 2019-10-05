from base_algorithm import Algorithm

class EGreedyAlgorithm(Algorithm):

    def __init__(self, e:float=0.1, k:int=10, optimistic:bool=False):
        super(Algorithm, self).__init__(k, optimistic)
        self.e = e

    def action_arm(self) -> int:
        pass

    def learn_arm(self, arm_no: int, reward: int) -> None:
        pass