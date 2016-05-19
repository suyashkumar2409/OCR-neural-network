import numpy as np

class Network(object):
	def __init__(self,sizes):
	
	####Sizes is a list of list, where each element gives you num of neurons in that layer ##########
		self.sizes = sizes
		self.num_layers = len(sizes)
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		### If aX1 and bX1 then weight is bXa ###
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])
		
		
