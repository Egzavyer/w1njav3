import socket
import select


class SocketInterface:
    def __init__(self):
        self.udpPort = 8080
        self.tcpClientPort = 8081
        self.tcpServerPort = 8082
        self.localIP = self.getOwnIP()
        self.initSockets()

    def initSockets(self):
        self.udpSocket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )
        self.udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.udpSocket.bind((self.localIP, self.udpPort))

        self.tcpServerSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
        )
        self.tcpServerSocket.bind((self.localIP, self.tcpServerPort))

    def broadcast(self, msg: str):
        self.udpSocket.sendto(msg.encode(), ("255.255.255.255", self.udpPort))

    def sendDataUDP(self, msg, destination):
        self.udpSocket.sendto(msg.encode(), destination)

    def receiveDataUDP(self):
        data, senderAddr = self.udpSocket.recvfrom(1024)
        return data, senderAddr

    def getOwnIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print("Local IP: ", ip)
        return ip
