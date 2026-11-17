[app]

# (str) Title of your application
title = REDX Super Assistant

# (str) Package name
package.name = redxassistant

# (str) Package domain (needed for android packaging)
package.domain = org.redx

# (str) Source files to include (let it be empty to include all)
source.dir = .

# (list) Source files to include (let it be empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (int) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
# android.sdk = 20

# (str) Android NDK version to use
# android.ndk = 25b

