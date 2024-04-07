import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    else:
        list = np.array(list).reshape(3,3)
        calculations = {
            'mean' : [np.mean(list, axis=x).tolist() for x in [0, 1, None]],
            'variance' : [np.var(list, axis=x).tolist() for x in [0, 1, None]],
            'standard deviation' : [np.std(list, axis=x).tolist() for x in [0, 1, None]],
            'max' : [np.max(list, axis=x).tolist() for x in [0, 1, None]],
            'min' : [np.min(list, axis=x).tolist() for x in [0, 1, None]],
            'sum' : [np.sum(list, axis=x).tolist() for x in [0, 1, None]]
        }
    return calculations