from base_algorithm import Algorithm

class KArmedBandit:

    def __init__(self, algorithm:Algorithm, k:int=10, stationary:bool=True) -> None:

        self.k = k
        self._strategy = algorithm