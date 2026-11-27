[app]

title = REDX Assistant
package.name = redxassistant
package.domain = org.redx

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 0.1

requirements = python3,kivy,charset-normalizer<3.5.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 27.2.12479018
android.ndk_api = 24
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
android.permissions = INTERNET

