from PeerDiscovery import *
from SocketInterface import *
from ConnectionHandler import *
from Peer import *


def main():
    try:
        si = SocketInterface()
        pd = PeerDiscovery(si)
        ch = ConnectionHandler(si)
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
        while True:
            pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
