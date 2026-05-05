from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
class GhostHandshake:
    def __init__(self):
        self.private_key = None
        self.public_key = None
    def generate_node_keys(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()
        print("[+] RSA Node Keys Generated Successfully.")