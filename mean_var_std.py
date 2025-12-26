import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("Please enter exactly 9 integers separated by commas.")

    a = np.array(list).reshape((3, 3))

    calculations = {
        'mean': [
            np.mean(a, axis=0).tolist(),
            np.mean(a, axis=1).tolist(),
            np.mean(a).item() 
        ],
        'variance': [
            np.var(a, axis=0).tolist(),
            np.var(a, axis=1).tolist(),
            np.var(a).item()
        ],
        'standard deviation': [
            np.std(a, axis=0).tolist(),
            np.std(a, axis=1).tolist(),
            np.std(a).item()
        ],
        'max': [
            np.max(a, axis=0).tolist(),
            np.max(a, axis=1).tolist(),
            np.max(a).item()
        ],
        'min': [
            np.min(a, axis=0).tolist(),
            np.min(a, axis=1).tolist(),
            np.min(a).item()
        ],
        'sum': [
            np.sum(a, axis=0).tolist(),
            np.sum(a, axis=1).tolist(),
            np.sum(a).item()
        ]
    }
    return calculations
