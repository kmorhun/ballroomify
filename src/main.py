import numpy as np

def evaluate(style, rankings):
    """
    Docstring style: reST.
    given a list of rankings for a particular style, 
    returns the dancers average ranking and prints the result out.
    
    :param style: the style performed
    :type style: Style
    :param rankings: a list of numbers from scores received by calling perform() on dances
    :type rankings: List[int]
    :return: None
    """
    avg = np.average(rankings)
    print(f"Your average ranking in {style.name} was {avg}")