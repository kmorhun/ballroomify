from abc import ABC, abstractmethod
import numpy as np

class Style(ABC):
    """
        An abstract Style class that defines what all Styles should be capble of
    """
    @abstractmethod
    def compete(self):
        """
            An abstract compete method for instantiated styles to populate
        """
        pass

class Dance():
    def __init__(self, name, time_signature, bpm):
        """
        Docstring style: reST.
        Creates a Dance Object
        
        :param name: the name of the dance
        :type name: string
        :param style: the style of the dance
        :type style: Style
        :param time_signature: the time signature of the dance
        :type time_signature: string
        :returns: None
        :rtype: None
        """
        self.name = name
        self.time_signature = time_signature
        self.bpm = bpm
    
    def perform(self):
        """
        Prints a string describing the performance of this dance
        of the format "Performing {name} at {number} bpm"
        """
        print(f"Performing {self.name} at {self.bpm} bpm")

class InternationalStandard(Style):
    def __init__(self, dances):
        """
        Docstring style: Google
        """
        self.dances = dances
        self.name = "International Standard"
    
    def compete(self):
        """
        Docstring style: NumPy
        """
        for dance in self.dances:
            dance.perform()
        rankings = np.random.randint(low=1, high=8, size=len(self.dances))
        return rankings
        

        


