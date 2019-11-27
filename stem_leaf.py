# get stem leaf plot in dictionary
def stemleaf(data):
	stem_leaf = {}
	for x in data:
		x_str = str(x)
		if (len(x_str) == 1):
			x_str = "0" + x_str
	
		stem = int(x_str[:-1])
		leaf = int(x_str[-1])
	
		if (stem not in stem_leaf):
			stem_leaf[stem] = [leaf]
		else:
			stem_leaf[stem] = stem_leaf[stem] + [leaf]
	return stem_leaf
