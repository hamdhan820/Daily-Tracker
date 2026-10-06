import sys, re
p = sys.argv[1] if len(sys.argv) > 1 else "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()
perms = [
 "android.permission.SCHEDULE_EXACT_ALARM",
 "android.permission.USE_EXACT_ALARM",
 "android.permission.USE_FULL_SCREEN_INTENT",
 "android.permission.POST_NOTIFICATIONS",
 "android.permission.RECEIVE_BOOT_COMPLETED",
 "android.permission.WAKE_LOCK",
 "android.permission.VIBRATE",
]
add = "".join(f'    <uses-permission android:name="{x}" />\n' for x in perms if x not in s)
if add:
    s = re.sub(r"(<manifest[^>]*>\s*)", lambda m: m.group(1) + "\n" + add, s, count=1)
    open(p, "w", encoding="utf-8").write(s)
print("Patched" if add else "Already had all permissions")
