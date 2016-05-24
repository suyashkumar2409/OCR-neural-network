import quadcost
import crosscost
import mnistloader

trainingdata, validationdata, testingdata = mnistloader.load_data_wrapper()

net = crosscost.Network([784,30,10])

net.graddesc(trainingdata,30,10,0.02,testingdata)


#####Use learning rate 3 when using quadcost, and 0.005 while using crosscost for best results and avoiding under/overfitting
