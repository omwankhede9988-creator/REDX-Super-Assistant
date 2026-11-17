[app]

# (str) Title of your application
title = REDX Super Assistant

# (str) Package name
package.name = redxassistant

# (str) Package domain (needed for android packaging)
package.domain = org.redx

# (list) Source files to include (let it match your main file, e.g., main.py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Min API your APK will support
android.min_api = 21
