from base_algorithm import Algorithm

class UCBAlgorithm(Algorithm):

    def __init__(self, c:float=1.0, k:int=10, optimistic:bool=False):
        super(Algorithm, self).__init__(k, optimistic)
        self.c = c

    def action_arm(self) -> int:
        pass

    def learn_arm(self, arm_no: int, reward: int) -> None:
        pass