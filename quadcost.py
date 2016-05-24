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
		self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])

	def feedforward(self,x):
		for l in xrange(1,len(self.sizes)-1):
			x = sigmoid(np.dot(self.weights[l-1],x) + self.biases[l-1])
		
		return x

	def graddesc(self,x,y,epochs,minibatchsize,eta,trainingdata,testdata = None):
		traininglen = len(trainingdata)

		testlen = -1
		if testdata:
			testlen = len(testingdata)

		for i = xrange(1,epochs):
			random.shuffle(trainingdata)


			minibatches = [trainingdata[j:j+minibatchsize] for j in xrange(0,traininglen,minibatchsize)]

			for mini in minibatches:
				self.relax(mini,eta)

			if testdata:
				print "Epoch {0}: {1} / {2}".format(i,self.evaluate(testingdata),testlen)

			else:
				print "Epoch {0}".format(i)

	def relax(self,mini,eta):
		biastemp = np.array([np.zeros(b.shape) for b in self.biases])
		weighttemp = np.array([np.zeros(w.shape) for w in self.weights])

		for x,y in mini:

			deltabias,deltaweight = self.backprop(x,y)

			biastemp = biastemp + np.array(deltabias)
	
			weighttemp = weighttemp + np.array(deltaweight)
			 
		biastemp = list(biastemp)
		weighttemp = list(weighttemp)

		self.biases = [b - (eta/len(mini)*db for b,db in zip(self.biases,biastemp)]
		self.weights = [w - (eta/len(mini)*dw for w,dw in zip(self.weights,weighttemp)]

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

		deltas = [np.zeros(a.shape) for a in activations]

		deltal = (activations[-1]-y)*sigmoidprime(zs[-1])
		
		bret[-1] = deltal

		wret[-1] = np.dot(deltal,activations[-2].transpose())

		deltas[-1] = deltal

		for i = xrange(2,len(self.weights)):
			deltacurr = np.dot(self.weights[-l+1].transpose,deltas[-l+1])*sigmoidprime(zs[-l])
			deltas[-l] = deltacurr

			bret[-l] = deltacurr

			wret[-l] = np.dot(deltacurr,activations[-l-1].transpose())

		return bret,wret
				

