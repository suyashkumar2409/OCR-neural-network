import quadcost
import mnistloader

trainingdata, validationdata, testingdata = mnistloader.load_data_wrapper()

net = quadcost.Network([784,30,10])

net.graddesc(trainingdata,30,10,3.0,testingdata)


