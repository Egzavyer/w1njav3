from threading import Thread


class Peer:
    def __init__(self, pd, ch):
        self.pd = pd
        self.ch = ch

    def startPeer(self):
        pdThread = Thread(target=self.pd.discoverPeers)
        chThread = Thread(target=self.ch.handleConnection)
        pdThread.daemon = True
        chThread.daemon = True
        pdThread.start()
        chThread.start()

    def choosePeer(self):
        peerMap = {}
        self.pd.mutex.acquire()
        i = 0
        print("Choose a peer to connect to or press 'r' to refresh the list of peers")
        print("+----------------------------+")
        for peer in self.pd.peerTable:
            peerMap[str(i)] = peer
            print("| " + str(i) + " | " + peer + " |")
            i += 1
        print("+----------------------------+")
        self.pd.mutex.release()
        return peerMap

    def connectToPeer(self, peerIP: str):
        self.ch.connectTo(peerIP, self.pd.peerTable[peerIP])
