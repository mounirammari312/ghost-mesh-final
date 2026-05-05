from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

class GhostHandshake:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_node_keys(self):
        try:
            # تم إضافة backend=default_backend() لضمان التوافق مع Buildozer Recipes
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            self.public_key = self.private_key.public_key()
            print("[+] RSA Node Keys Generated Successfully.")
        except Exception as e:
            # رفع الاستثناء ليتم التقاطه في الواجهة الرسومية
            raise Exception(f"RSA Engine Failure: {str(e)}")
