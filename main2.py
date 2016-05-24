import quadcost
import quadcost2
import mnistloader

trainingdata, validationdata, testingdata = mnistloader.load_data_wrapper()

net = quadcost2.Network([784,30,10])

net.SGD(trainingdata,30,10,3.0,testingdata)


