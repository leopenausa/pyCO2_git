import numpy as np

def random_normal(mean, stdev, error):
    """Computes random number from interval with normal gaussian probability given mean and 2SD stdev"""
    res = 0
    np.random.seed()

    if error == "absolute":
        res = np.random.normal(mean, stdev / 2)  # for 2sigma inputs
        return res
    elif error == "rsd":
        res = np.random.normal(mean, mean * (stdev / 2))   # for 2sigma inputs
        return res
    
def random_flat(mean, stdev, error):
    """Computes random number from interval with flat distribution probability given mean and 2SD stdev"""
    res = 0
    np.random.seed()

    if error == "absolute":
        res = np.random.uniform(mean - stdev / 2, mean + stdev / 2)    # for 2sigma inputs
        return res
    elif error == "rsd":
        res = np.random.uniform(mean - (mean * stdev / 2), mean + (mean * stdev / 2))    # for 2sigma inputs
        return res