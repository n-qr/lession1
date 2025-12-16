import os

old_name = "main.exe"
new_name = "main.scr"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully!")
    input()
else:
    print("lession.exe not found")
