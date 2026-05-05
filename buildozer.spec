[app]
title = Ghost Mesh
package.name = ghostmesh
package.domain = net.ghostalgeria
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# الاعتماديات السيادية (تم إضافة kivy لضمان بقاء التطبيق حياً)
requirements = python3,kivy,cryptography,pyopenssl,certifi,setuptools

orientation = portrait
fullscreen = 1

# معمارية المعالجات الحديثة
android.archs = arm64-v8a, armeabi-v7a

# الصلاحيات المطلوبة للعمل الشبكي
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK

# تعريف الخدمة الخلفية (اختياري ولكن يدعم الاستقرار)
services = GhostEngine:main.py

# إعدادات المترجم
android.api = 31
android.minapi = 21
android.sdk = 36
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
