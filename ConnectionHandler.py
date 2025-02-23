from SocketInterface import *
from FileHandler import *


class ConnectionHandler:
    def __init__(self, si: SocketInterface, fh: FileHandler):
        self.si = si
        self.fh = fh

    def handleConnection(self):
        # TODO: handle connections in new threads
        client = self.si.acceptSocketConnection()
        while 1:
            self.receiveFile("Hello2.txt", self.si.receiveDataTCP(client))

    def connectTo(self, ip, port):
        self.ip = ip
        self.port = port
        self.si.connectToSocket(self.ip, self.port)

    def sendFile(self, filename):
        # TODO: fragment files
        data, dataSize = self.fh.loadFile(filename)
        print(data)
        print(dataSize)
        bytesSent, bytesRemaining = 0, dataSize
        while bytesSent < dataSize:
            if bytesRemaining <= 576:
                fragment = data[bytesSent:]
            else:
                fragment = data[bytesSent : bytesSent + 576]
            self.si.sendDataTCP(
                self.si.tcpClientSocket,
                fragment,
                (self.ip, int(self.port)),
            )
            bytesSent += len(fragment)
        print("File Transmission Complete")

    def receiveFile(self, filename, data):
        self.fh.writeFile(filename, data)
