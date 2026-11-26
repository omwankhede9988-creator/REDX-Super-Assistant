[app]

title = REDX Super Assistant
package.name = redxassistant
package.domain = org.redx

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3,ogg
source.exclude_dirs = tests,bin,venv,.git,__pycache__

version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
