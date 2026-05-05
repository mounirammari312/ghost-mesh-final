import socket, select, threading
class GhostTunnel:
    def __init__(self, host="127.0.0.1", port=9050):
        self.host, self.port, self.running = host, port, True
    def handle_client(self, connection):
        try:
            connection.recv(2); connection.sendall(b"\x05\x00")
            data = connection.recv(4)
            if not data: return
            addr_type = data[3]
            if addr_type == 1: addr = socket.inet_ntoa(connection.recv(4))
            elif addr_type == 3: addr = connection.recv(connection.recv(1)[0]).decode()
            port = int.from_bytes(connection.recv(2), "big")
            remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote.connect((addr, port))
            connection.sendall(b"\x05\x00\x00\x01" + socket.inet_aton("0.0.0.0") + (0).to_bytes(2, "big"))
            self.exchange_data(connection, remote)
        except: pass
        finally: connection.close()
    def exchange_data(self, client, remote):
        while self.running:
            r, w, e = select.select([client, remote], [], [])
            if client in r:
                data = client.recv(4096)
                if not data or remote.send(data) <= 0: break
            if remote in r:
                data = remote.recv(4096)
                if not data or client.send(data) <= 0: break
    def start_proxy(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port)); s.listen(20)
        while self.running:
            c, a = s.accept()
            threading.Thread(target=self.handle_client, args=(c,), daemon=True).start()