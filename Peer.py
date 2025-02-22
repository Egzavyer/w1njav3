from threading import Thread


class Peer:
    def __init__(self, pd):
        self.pd = pd

    def startPeer(self):
        pdThread = Thread(target=self.pd.discoverPeers)
        pdThread.daemon = True
        pdThread.start()

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
