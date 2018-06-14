from network.network import Network
from network.layers.layer import Layer
from network.connections.connection import Connection

def main():
    n = Network()
    l1 = Layer(4)
    l2 = Layer(1)
    c = Connection(l1, l2)
    n.addHiddenLayer(l1)
    n.addHiddenLayer(l2)
    n.addConnection(c)
    
if __name__ == "__main__":
    main()
