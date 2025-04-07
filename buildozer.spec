[app]
title = SMS Reader
package.name = smsreader
package.domain = org.bidu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = requirements = python3,kivy,android,jnius
android.permissions = READ_SMS
orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.sdk = 30
