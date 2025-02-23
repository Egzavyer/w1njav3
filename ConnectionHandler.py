from SocketInterface import *
from FileHandler import *


class ConnectionHandler:
    def __init__(self, si: SocketInterface, fh: FileHandler):
        self.si = si
        self.fh = fh

    def handleConnection(self):
        # TODO: handle connections in new threads
        self.receiveFile(
            "Hello2.txt", self.si.receiveDataTCP(self.si.acceptSocketConnection())
        )

    def connectTo(self, ip, port):
        self.ip = ip
        self.port = port
        self.si.connectToSocket(self.ip, self.port)

    def sendFile(self, filename):
        # TODO: fragment files
        self.si.sendDataTCP(
            self.si.tcpClientSocket,
            self.fh.loadFile(filename),
            (self.ip, int(self.port)),
        )

    def receiveFile(self, filename, data):
        self.fh.writeFile(filename, data)
