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
		for l in xrange(1,len(self.sizes)-1):
			x = sigmoid(np.dot(self.weights[l-1],x) + self.biases[l-1])
		
		return x
	
	def graddesc(self,trainingdata,epochs,minibatchsize,eta,testdata = None):
		traininglen = len(trainingdata)

		testlen = -1
		if testdata:
			testlen = len(testdata)

		for i in xrange(1,epochs):
			random.shuffle(trainingdata)


			minibatches = [trainingdata[j:j+minibatchsize] for j in xrange(0,traininglen,minibatchsize)]

			for mini in minibatches:
				self.update_mini_batch(mini,eta)

			if testdata:
				print "Epoch {0}: {1} / {2}".format(i,self.evaluate(testdata),testlen)

			else:
				print "Epoch {0}".format(i)
				
	def update_mini_batch(self, mini_batch, eta):
		nabla_b = [np.zeros(b.shape) for b in self.biases]
		nabla_w = [np.zeros(w.shape) for w in self.weights]
		for x, y in mini_batch:
			delta_nabla_b, delta_nabla_w = self.backprop(x, y)
			nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
			nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
		self.weights = [w-(eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
		self.biases = [b-(eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]

	def relax(self,mini,eta):	
		for x,y in mini:

			deltabias,deltaweight = self.backprop(x,y)

			biastemp = biastemp + np.array(deltabias)
	
			weighttemp = weighttemp + np.array(deltaweight)
			 
		biastemp = list(biastemp)
		weighttemp = list(weighttemp)

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

		deltas = [np.zeros(a.shape) for a in activations]

		deltal = (activations[-1]-y)*sigmoidderiviative(zs[-1])
		
		bret[-1] = deltal

		wret[-1] = np.dot(deltal,activations[-2].transpose())

		deltas[-1] = deltal

		for i in xrange(2,len(self.weights)):
			deltacurr = np.dot(self.weights[-l+1].transpose,deltas[-l+1])*sigmoidprime(zs[-l])
			deltas[-l] = deltacurr

			bret[-l] = deltacurr

			wret[-l] = np.dot(deltacurr,activations[-l-1].transpose())

		return bret,wret
				

