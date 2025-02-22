from PeerDiscovery import *
from SocketInterface import *
from Peer import *


def main():
    try:
        si = SocketInterface()
        pd = PeerDiscovery(si)
        peer = Peer(pd)
        peer.startPeer()
        while len(peer.pd.peerTable) == 0:
            pass
        peerChoice = "r"
        while peerChoice == "r":
            peerMap = peer.choosePeer()
            peerChoice = input("")
        print("Chosen Peer: " + peerMap[peerChoice])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
