from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


# a client protocol


class Client(protocol.Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)
    def dataReceived(self, data):
        data = data.decode("utf-8")  # convert data into string
        print(data)
    def send_data(self):
        while True:
            self.transport.write(input().encode('utf-8'))


class ClientFactory(protocol.ClientFactory):  # create a instance of Client

    def buildProtocol(self, addr):
        return Client()


if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, 'localhost', 2000)  # connect endpoint of the client to the local host
    cf = ClientFactory()
    endpoint.connect(cf)  # endpoint connect with instance of Client
    reactor.run()