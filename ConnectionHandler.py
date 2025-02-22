from SocketInterface import *


class ConnectionHandler:
    def __init__(self, si: SocketInterface):
        self.si = si

    def handleConnection(self):
        print(self.si.receiveDataTCP(self.si.acceptSocketConnection()))

    def connectTo(self, ip, port):
        self.si.connectToSocket(ip, port)
        self.si.sendDataTCP(self.si.tcpClientSocket, "Hello, World", (ip, int(port)))
        # self.si.sendDataTCPClient("Hello, World", (ip, int(port)))
