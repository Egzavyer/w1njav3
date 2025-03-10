import socket

SOCKET_BACKLOG = 3


class SocketInterface:
    def __init__(self):
        self.udpPort = 8080
        self.tcpClientPort = 8081
        self.tcpServerPort = 8082
        self.localIP = self.getOwnIP()
        self.udpSocket = self.initUDPSocket()
        self.tcpServerSocket = self.initTCPServerSocket()
        self.tcpClientSocket = self.initTCPClientSocket()

    def initUDPSocket(self):
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        udpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udpSocket.bind((self.localIP, self.udpPort))
        return udpSocket

    def initTCPServerSocket(self):
        tcpServerSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
        )
        tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServerSocket.bind((self.localIP, self.tcpServerPort))
        tcpServerSocket.listen(SOCKET_BACKLOG)
        return tcpServerSocket

    def initTCPClientSocket(self):
        tcpClientSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP
        )
        tcpClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpClientSocket.bind((self.localIP, self.tcpClientPort))
        return tcpClientSocket

    def broadcast(self, msg: str):
        self.udpSocket.sendto(msg.encode(), ("255.255.255.255", self.udpPort))

    def sendDataUDP(self, msg, destination):
        self.udpSocket.sendto(msg.encode(), destination)

    def receiveDataUDP(self):
        data, senderAddr = self.udpSocket.recvfrom(1024)
        return data, senderAddr

    def acceptSocketConnection(self):
        client, addr = self.tcpServerSocket.accept()
        return client

    def receiveDataTCP(self, conn: socket):
        data = conn.recv(1024)
        return data

    def connectToSocket(self, ip, port):
        self.tcpClientSocket.connect((ip, int(port)))
        print("Connected to: " + ip + "::" + port)

    def sendDataTCP(self, socket: socket, msg: bytes, destination):
        socket.sendto(msg, destination)

    def getOwnIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        print("Local IP: ", ip)
        return ip
