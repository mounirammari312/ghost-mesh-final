import threading
import sys
import time
import os

# إعداد المسارات المطلقة لضمان عمل الاستيراد في بيئة أندرويد المعزولة
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

# استيراد المكونات السيادية للنظام
from security.handshake import GhostHandshake
from core.discovery import GhostDiscovery
from core.tunnel import GhostTunnel

class GhostMeshApp(App):
    def build(self):
        self.title = "GHOST-MESH V1.0"
        self.label = Label(
            text="[GHOST-MESH]\nSYSTEM BOOTING...",
            halign="center",
            font_size='16sp'
        )
        return self.label

    def on_start(self):
        # تشغيل المحرك في خيط مستقل لضمان استجابة الواجهة الرسومية
        threading.Thread(target=self.run_system_core, daemon=True).start()

    def update_ui_status(self, message):
        self.label.text = f"[GHOST-MESH]\n{message}"

    def run_system_core(self):
        try:
            Clock.schedule_once(lambda dt: self.update_ui_status("CORE INITIALIZING..."), 0)
            
            self.security = GhostHandshake()
            self.discovery = GhostDiscovery()
            self.tunnel = GhostTunnel()

            Clock.schedule_once(lambda dt: self.update_ui_status("GENERATING RSA ENGINE..."), 0)
            self.security.generate_node_keys()

            # إطلاق بروتوكولات الشبكة والاكتشاف
            threading.Thread(target=self.discovery.listen_for_peers, daemon=True).start()
            threading.Thread(target=self.tunnel.start_proxy, daemon=True).start()

            Clock.schedule_once(lambda dt: self.update_ui_status("STATUS: OPERATIONAL"), 0)

            while True:
                self.discovery.broadcast_presence("ALGERIA_CORE_PRIMARY")
                time.sleep(15)
                
        except Exception as e:
            # في حال حدوث خطأ، يتم عرضه فوراً على الشاشة للتشخيص
            Clock.schedule_once(lambda dt: self.update_ui_status(f"CRITICAL ERROR:\n{str(e)}"), 0)

if __name__ == "__main__":
    GhostMeshApp().run()
