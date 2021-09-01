import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  new_list = np.array(list)
  print(new_list)

  mean_axis1 = [new_list[[0,3,6]].mean(), new_list[[1,4,7]].mean(),new_list[[2,5,8]].mean()]
  mean_axis2 = [new_list[[0,1,2]].mean(), new_list[[3,4,5]].mean(),new_list[[6,7,8]].mean()]

  var_axis1 = [new_list[[0,3,6]].var(), new_list[[1,4,7]].var(),new_list[[2,5,8]].var()]
  var_axis2 = [new_list[[0,1,2]].var(), new_list[[3,4,5]].var(),new_list[[6,7,8]].var()]

  std_axis1 = [new_list[[0,3,6]].std(), new_list[[1,4,7]].std(),new_list[[2,5,8]].std()]
  std_axis2 = [new_list[[0,1,2]].std(), new_list[[3,4,5]].std(),new_list[[6,7,8]].std()]

  max_axis1 = [new_list[[0,3,6]].max(), new_list[[1,4,7]].max(),new_list[[2,5,8]].max()]
  max_axis2 = [new_list[[0,1,2]].max(), new_list[[3,4,5]].max(),new_list[[6,7,8]].max()]

  min_axis1 = [new_list[[0,3,6]].min(), new_list[[1,4,7]].min(),new_list[[2,5,8]].min()]
  min_axis2 = [new_list[[0,1,2]].min(), new_list[[3,4,5]].min(),new_list[[6,7,8]].min()]

  sum_axis1 = [new_list[[0,3,6]].sum(), new_list[[1,4,7]].sum(),new_list[[2,5,8]].sum()]
  sum_axis2 = [new_list[[0,1,2]].sum(), new_list[[3,4,5]].sum(),new_list[[6,7,8]].sum()]




  return {
    'mean': [mean_axis1, mean_axis2, new_list.mean()],
    'variance': [var_axis1, var_axis2, new_list.var()],
    'standard deviation': [std_axis1, std_axis2, new_list.std()],  'max': [max_axis1, max_axis2, new_list.max()],
    'min': [min_axis1, min_axis2, new_list.min()],
    'sum': [sum_axis1, sum_axis2, new_list.sum()]

  } #calculations