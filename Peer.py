from threading import Thread


class Peer:
    def __init__(self, pd):
        self.pd = pd

    def startPeer(self):
        pdThread = Thread(target=self.pd.discoverPeers)
        pdThread.daemon = True
        pdThread.start()

    def choosePeer(self):
        self.pd.mutex.acquire()
        i = 0
        print("+----------------------------+")
        for peer in self.pd.peerTable:
            print("| " + str(i) + " | " + peer + " |")
            i += 1
        print("+----------------------------+")
        self.pd.mutex.release()
