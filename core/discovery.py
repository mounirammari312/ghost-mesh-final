import socket, time
class GhostDiscovery:
    def __init__(self, port=9090):
        self.port = port
    def broadcast_presence(self, node_id):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.sendto(f"GHOST_NODE:{node_id}".encode(), ("255.255.255.255", self.port))
    def listen_for_peers(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(("", self.port))
            while True:
                data, addr = s.recvfrom(1024)
                print(f"\n[!] Peer Discovered: {data.decode()} at {addr}")