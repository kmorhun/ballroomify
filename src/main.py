import numpy as np

def evaluate(style, rankings):
    avg = np.average(rankings)
    print(f"Your average ranking in {style.name} was {avg}")