class PeerDiscovery:
    def __init__(self, si):
        self.si = si
        self.peerTable = {}
        self.broadcastRequest()

    def discoverPeers(self):
        while True:
            data, peerAddress = self.si.receiveDataUDP()
            if data and peerAddress:
                if peerAddress[0] not in self.peerTable.keys():
                    self.peerTable[peerAddress[0]] = data.decode()[1:]
                    self.sendResponse(peerAddress)
                    print(self.peerTable)

    def broadcastRequest(self):
        self.si.broadcast("1" + str(self.si.tcpServerPort))

    def sendResponse(self, peerAddress):
        self.si.sendDataUDP("0" + str(self.si.tcpServerPort), peerAddress)
