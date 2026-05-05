[app]
title = Ghost Mesh
package.name = ghostmesh
package.domain = net.ghostalgeria
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,hostpython3,cryptography,pyopenssl,certifi,setuptools
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK
services = GhostEngine:main.py
[buildozer]
log_level = 2
warn_on_root = 0
