import numpy as np

def calculate(list1):
    if len(list1) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        np_list = np.reshape(np.array(list1), [3,3])
        calculations = {
          'mean': [list(np_list.mean(axis = 0)), list(np_list.mean(axis = 1)), np_list.mean()],
          'variance': [list(np_list.var(axis = 0)), list(np_list.var(axis = 1)), np_list.var()],
          'standard deviation': [list(np_list.std(axis = 0)), list(np_list.std(axis = 1)), np_list.std()],
          'max': [list(np_list.max(axis = 0)), list(np_list.max(axis = 1)), np_list.max()],
          'min': [list(np_list.min(axis = 0)), list(np_list.min(axis = 1)), np_list.min()],            
          'sum': [list(np_list.sum(axis = 0)), list(np_list.sum(axis = 1)), np_list.sum()],
            }

    return calculations

