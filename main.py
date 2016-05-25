import quadcost
import crosscost
import mnistloader
import crossregularization

trainingdata, validationdata, testingdata = mnistloader.load_data_wrapper()

net = crossregularization.Network([784,30,10])

net.graddesc(trainingdata,30,10,2.0,testingdata,lamda=1.0)


#####Use learning rate 3 when using quadcost, and 0.005 while using crosscost for best results and avoiding under/overfitting
