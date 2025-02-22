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
        peer.choosePeer()
        while True:
            pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
