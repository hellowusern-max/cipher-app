[app]
title = تطبيق التشفير
package.name = cipherapp
package.domain = com.hellowusern.cipher
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True