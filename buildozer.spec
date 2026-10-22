[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = kivypapp

# (str) Package domain (needed for android packaging)
package.domain = org.kivy

# (str) Source files where the let it go (relative to directory of spec)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
