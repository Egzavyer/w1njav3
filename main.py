import threading

from PeerDiscovery import *
from SocketInterface import *


def main():
    try:
        si = SocketInterface()
        pd = PeerDiscovery(si)

        t1 = threading.Thread(target=pd.discoverPeers)
        t1.start()
    except KeyboardInterrupt:
        t1.join()


if __name__ == "__main__":
    main()
