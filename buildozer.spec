[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = kivypackage

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the main.py file is located
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add other dependencies like kivymd if needed
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
# android.sdk = 20

# (str) ANT version to use
# android.ant_version = 1.9.4

# (bool) Use Android TabLayout
# android.tablayout = True

# (list) The Android archs to build for,, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

