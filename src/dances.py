from abc import ABC, abstractmethod
import numpy as np

class Style(ABC):
    @abstractmethod
    def compete():
        pass

class Dance():
    def __init__(self, name, time_signature, bpm):
        """
        Docstring style: reST.
        Creates a Dance Object
        :param name: the name of the dance
        :param time_signature: the time signature of the dance
        :returns: None
        """
        self.name = name
        self.time_signature = time_signature
        self.bpm = bpm
    
    def perform(self):
        print(f"Performing {self.name} at {self.bpm} bpm")


class InternationalStandard(Style):
    def __init__(self, dances):
        self.dances = dances
        self.name = "International Standard"
    
    def compete(self):
        for dance in self.dances:
            dance.perform()
        rankings = np.random.randint(low=1, high=8, size=len(self.dances))
        return rankings
        

        


