import threading, sys, time, os
sys.path.append(".")
from security.handshake import GhostHandshake
from core.discovery import GhostDiscovery
from core.tunnel import GhostTunnel

class GhostMeshApp:
    def __init__(self):
        self.node_id = "ALGERIA_CORE_PRIMARY"
        self.security = GhostHandshake()
        self.discovery = GhostDiscovery()
        self.tunnel = GhostTunnel()
        self.running = True

    def start(self):
        print("\n" + "="*50 + "\n   GHOST-MESH: SYSTEM FULLY OPERATIONAL\n" + "="*50)
        self.security.generate_node_keys()
        threading.Thread(target=self.discovery.listen_for_peers, daemon=True).start()
        threading.Thread(target=self.tunnel.start_proxy, daemon=True).start()
        try:
            while self.running:
                self.discovery.broadcast_presence(self.node_id)
                time.sleep(10)
        except KeyboardInterrupt: self.running = False

if __name__ == "__main__":
    app = GhostMeshApp()
    app.start()