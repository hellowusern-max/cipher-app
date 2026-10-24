[app]
title = YT Loader
package.name = ytloader
package.domain = com.amar.ytloader
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,db
version = 1.0
requirements = python3,kivy,flask,flask_cors,requests,android,sqlite3
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# p4a
p4a.url = https://github.com/kivy/python-for-android
p4a.branch = master
p4a.bootstrap = sdl2
p4a.port = 5000

[app:android]
permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.ant = auto
