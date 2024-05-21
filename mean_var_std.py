import numpy as np

def calculate(data: list) -> dict:
    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")
    
    dataarray = np.array(data).reshape((3,3))
    print(dataarray)

    
    calculations = {
        'mean': [list(dataarray.mean(axis=0)), list(dataarray.mean(axis=1)), dataarray.mean()],
        'variance': [list(dataarray.var(axis=0)), list(dataarray.var(axis=1)), dataarray.var()],
        'standard deviation': [list(dataarray.std(axis=0)), list(dataarray.std(axis=1)), dataarray.std()],
        'max': [list(dataarray.max(axis=0)), list(dataarray.max(axis=1)), dataarray.max()],
        'min': [list(dataarray.min(axis=0)), list(dataarray.min(axis=1)), dataarray.min()],
        'sum': [list(dataarray.sum(axis=0)), list(dataarray.sum(axis=1)), dataarray.sum()]
    }
        
    return calculations
