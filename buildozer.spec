[app]

# (str) Title of your application
title = REDX Super Assistant

# (str) Package name
package.name = redxassistant

# (str) Package domain (needed for android packaging)
package.domain = org.redx

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it match your main file, e.g., main.py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of directory to exclude (optional)
source.exclude_dirs = bin venv .git

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning
version = 0.1

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible
android.api = 33

# (int) Min API your APK will support
android.min_api = 21

# (str) Android SDK version to use
# android.sdk = 33

# (str) Supported View/Build tools version (optional)
android.build_tools_version = 33.0.2
