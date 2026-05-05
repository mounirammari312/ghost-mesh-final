import threading
import sys
import time
import os

# إدماج المسارات لضمان وصول المجمّع للمجلدات الفرعية في أندرويد
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

# استيراد المحركات السيادية
from security.handshake import GhostHandshake
from core.discovery import GhostDiscovery
from core.tunnel import GhostTunnel

class GhostMeshApp(App):
    def build(self):
        # واجهة النظام البسيطة لضمان استقرار النشاط
        self.title = "GHOST-MESH CORE"
        self.label = Label(
            text="[GHOST-MESH]\nINITIALIZING SYSTEM...",
            halign="center",
            font_size='18sp'
        )
        return self.label

    def on_start(self):
        # إطلاق المحرك البرمجي في خيط منفصل لمنع تجميد الواجهة
        threading.Thread(target=self.initialize_engine, daemon=True).start()

    def update_status(self, message):
        # تحديث الواجهة من خلال خيط Kivy الرئيسي
        self.label.text = f"[GHOST-MESH]\nSTATUS: {message}"

    def initialize_engine(self):
        try:
            Clock.schedule_once(lambda dt: self.update_status("BOOTING CORE..."), 0)
            
            # إعداد الهوية السيادية للعقدة
            self.node_id = "ALGERIA_CORE_PRIMARY"
            self.security = GhostHandshake()
            self.discovery = GhostDiscovery()
            self.tunnel = GhostTunnel()

            # توليد مفاتيح RSA
            Clock.schedule_once(lambda dt: self.update_status("GENERATING RSA KEYS..."), 0)
            self.security.generate_node_keys()

            # تفعيل بروتوكولات الاكتشاف والنفق
            threading.Thread(target=self.discovery.listen_for_peers, daemon=True).start()
            threading.Thread(target=self.tunnel.start_proxy, daemon=True).start()

            Clock.schedule_once(lambda dt: self.update_status("SYSTEM OPERATIONAL"), 0)

            # حلقة البث المستمر
            while True:
                self.discovery.broadcast_presence(self.node_id)
                time.sleep(15)
                
        except Exception as e:
            error_msg = f"CRITICAL ERROR: {str(e)}"
            Clock.schedule_once(lambda dt: self.update_status(error_msg), 0)

if __name__ == "__main__":
    GhostMeshApp().run()
