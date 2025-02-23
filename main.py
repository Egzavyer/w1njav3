from PeerDiscovery import *
from SocketInterface import *
from ConnectionHandler import *
from Peer import *
from FileHandler import *


def main():
    try:
        fh = FileHandler("files")
        si = SocketInterface()
        pd = PeerDiscovery(si)
        ch = ConnectionHandler(si, fh)
        peer = Peer(pd, ch)

        peer.startPeer()
        while len(peer.pd.peerTable) == 0:
            pass
        peerChoice = "r"
        while peerChoice == "r":
            peerMap = peer.choosePeer()
            peerChoice = input("")
        print("Chosen Peer: " + peerMap[peerChoice])
        peer.connectToPeer(peerMap[peerChoice])
        peer.chooseFile()
        while True:
            pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
