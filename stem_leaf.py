
def stem_leaf(data):
  final = {}

  for x in data:
    x_str = str(x)
    if (len(x_str) == 1):
      x_str = "0" + x_str

    stem = x_str[:-1]
    leaf = x_str[-1]

    if (stem not in final):
      final[int(stem)] = [int(leaf)]
    else:
      final[int(stem)] = final[int(stem)] + [int(leaf)]
      
    return final
