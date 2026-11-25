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

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT_TO_PY2

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android presplash)
#android.presplash_color = #FFFFFF

# (string) Presplash animation effect (fade, slide, none)
#android.presplash_animation = fade

# (list) Permissions
# (lists of integers)
#android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) features (adds uses-feature -android:glEsVersion to manifest)
#android.features = android.hardware.type.watch

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (int) Android SDK version to use
#android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.min_api.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android entry point, default is ok for kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Full names of android libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7a/*.so
#android.add_libs_arm64_v8a = libs/android-v8a/*.so
#android.add_libs_x86 = libs/x86/*.so
#android.add_libs_mips = libs/mips/*.so

# (list) RecyclerView dependency
#android.gradle_dependencies =

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) Application requirements (comma separated e.g: requirements = sqlite3,kivy)
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash format (png or jpg)
#android.presplash_format = png

# (str) RegEx to match files to exclude from the run furthermore
#android.add_ exclusions =

# (str) Str to add to the application manifest
#android.add_manifest_xml =

# (str) Str to add to the application gradle build file (before dependencies)
#android.add_gradle_repositories =

# (str) Str to add to the application gradle build file (after dependencies)
#android.add_gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' dependency, or when using KivyMD.
#android.enable_androidx = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables auto-approval of licenses during SDK/NDK installation
android.accept_sdk_license = True

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) overrides the commit/branch to use for p4a
#p4a.commit =

# (str) The directory in which python-for-android should look for your own build recipes (optional)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
#p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port choice for buildozer
#p4a.port =

# (bool) Indicate whether the screen should stay awake
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the project.properties)
#android.add_aars =

# (list) Gradle dependencies to add (per Android SDK)
#android.gradle_dependencies =

# (bool) Copy files to assets folder instead of libs folder
#android.copy_assets_to_libs = False

# (str) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# (deprecated, use android.archs instead)
#arch = arm64-v8a

# (list) list of Java files to add to the android project (can be jar or a directory containing jars)
#android.add_src =

# (list) Android packaging options to add
#android.add_aars =

# (list) Indicate which Android ABI to use when building native libraries
#android.abi =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if run as root (0 = no, 1 = yes)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
#bin_dir = ./bin

# (str) Path to build directory (ignored on Android)
#build_dir = ./.buildozer
