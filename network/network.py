#! python
        
class Network:
    def __init__(self):
        self.inputLayer = None
        self.outputLayer = None
        self.hiddenLayers = []
        self.connections = []

    def setInputLayer(self, inputLayer):
        self.inputLayer = inputLayer

    def setOutputLayer(self, outputLayer):
        self.outputLayer = outputLayer

    def addHiddenLayer(self, layer):
        for existingLayer in self.hiddenLayers:
            if layer.name == existingLayer.name:
                return 0
        self.hiddenLayers.append(layer)
        return 1

    def addConnection(self, connection):
        self.connections.append(connection)
        for layer in self.hiddenLayers:
            if connection.l1 == layer:
                 print("hello")
    
