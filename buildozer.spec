[app]

# (str) Title of your application
title = REDX Super Assistant

# (str) Package name
package.name = redxassistant

# (str) Package domain (needed for android packaging)
package.domain = org.redx

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3,ogg

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements (comma separated e.g. requirements = sqlite3,kivy)
requirements = python3,kivy

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# OSX Specific
#
#

#
# Android specific
#
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.min_api.
android.ndk_api = 21

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables auto-approval of licenses during SDK/NDK installation
android.accept_sdk_license = True

# (str) Android SDK path
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if run as root (0 = no, 1 = yes)
warn_on_root = 1

