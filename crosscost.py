import numpy as np
import random

def sigmoid(x):
	return 1.0/(1.0+np.exp(-x))

def sigmoidderiviative(x):
	temp = sigmoid(x)

	return (1.0-temp)*temp

	
class Network(object):
	def __init__(self,sizes):
	
	####Sizes is a list of list, where each element gives you num of neurons in that layer ##########
		self.sizes = sizes
		self.num_layers = len(sizes)
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		### If aX1 and bX1 then weight is bXa ###
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])]


	def evaluate(self,testingdata):	
		testresults = [(np.argmax(self.feedforward(x)),y) for (x,y) in testingdata]
		
		
		return sum(int(x==y) for (x,y) in testresults)
		
	def feedforward(self,x):
	
		a = x
		for b,w in zip(self.biases,self.weights):
			a = sigmoid(np.dot(w,a) + b)
		
		return a
	
	def graddesc(self,trainingdata,epochs,minibatchsize,eta,testdata = None):
		traininglen = len(trainingdata)

		testlen = -1
		if testdata:
			testlen = len(testdata)

		for i in xrange(1,epochs):
			random.shuffle(trainingdata)


			minibatches = [trainingdata[j:j+minibatchsize] for j in xrange(0,traininglen,minibatchsize)]

			for mini in minibatches:
				self.relax(mini,eta)

			if testdata:
				print "Epoch {0}: {1} / {2}".format(i,self.evaluate(testdata),testlen)

			else:
				print "Epoch {0}".format(i)
				
	def relax(self,mini,eta):	
		biastemp = ([np.zeros(b.shape) for b in self.biases])
		weighttemp = ([np.zeros(w.shape) for w in self.weights])
	
		for x,y in mini:

			deltabias,deltaweight = self.backprop(x,y)

			biastemp = [b+db for b,db in zip(biastemp,deltabias)]
	
			weighttemp = [w+dw for w,dw in zip(weighttemp,deltaweight)]
			 
		self.biases = [b - (eta/len(mini))*db for b,db in zip(self.biases,biastemp)]
		self.weights = [w - (eta/len(mini))*dw for w,dw in zip(self.weights,weighttemp)]

        
        
	def backprop(self,x,y):
		bret = [np.zeros(b.shape) for b in self.biases]
		wret = [np.zeros(w.shape) for w in self.weights]

		activations = [x]
		zs = []

		lastactivation = x
		for b,w in zip(self.biases,self.weights):
			z = np.dot(w,lastactivation) + b
			a = sigmoid(z)

			activations.append(a)
			zs.append(z)

			lastactivation = a


		delta = (activations[-1]-y)#*sigmoidderiviative(zs[-1])
		
		bret[-1] = delta

		wret[-1] = np.dot(delta,activations[-2].transpose())
		for l in xrange(2,self.num_layers):
			delta = np.dot(self.weights[-l+1].transpose(),delta)#*sigmoidderiviative(zs[-l])
	
			bret[-l] = delta
			wret[-l] = np.dot(delta,activations[-l-1].transpose())

		return bret,wret
				

