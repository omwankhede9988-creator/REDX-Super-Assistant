[app]

# (str) Title of your application
title = REDX Assistant

# (str) Package name
package.name = redxassistant

# (str) Package domain (needed for android/ios packaging)
package.domain = org.redx

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (str) Presplash of your application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of your application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your compiler will support.
android.minapi = 24

# (int) Android SDK version to use
# android.sdk = 20

# (str) Android NDK version to use
android.ndk = 27.2.12479018

# (int) Android NDK API to use. This is the minimum API you want your SDK
# to support, usually the same as android.minapi.
android.ndk_api = 24

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (list) Permissions
android.permissions = INTERNET

# (list) features (adds uses-feature -xml to manifest)
# android.features = android.hardware.type.watch

# (int) launchMode to use for the activity
# android.launchMode = singleTop

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a link
# android.copy_libs = 1

# (list) The Android archs to deploy for, doris/arm64-v8a/armeabi-v7a
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
