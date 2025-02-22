from threading import Lock


class PeerDiscovery:
    def __init__(self, si):
        self.si = si
        self.peerTable = {}
        self.mutex = Lock()
        self.broadcastRequest()

    def discoverPeers(self):
        while True:
            data, peerAddress = self.si.receiveDataUDP()
            if peerAddress[0] not in self.peerTable.keys():
                self.addPeer(peerAddress[0], data.decode()[1:])
                self.sendResponse(peerAddress)
                print(self.peerTable)

    def broadcastRequest(self):
        self.si.broadcast("1" + str(self.si.tcpServerPort))

    def sendResponse(self, peerAddress):
        self.si.sendDataUDP("0" + str(self.si.tcpServerPort), peerAddress)

    def addPeer(self, peerAddress, peerPort):
        self.mutex.acquire()
        self.peerTable[peerAddress] = peerPort
        self.mutex.release()
