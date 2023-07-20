import os
os.system("git pull origin main")
for file in os.listdir("."):
    if '.' not in file:
        new_file = file + ".png"
        os.rename(file, new_file)
os.system("git add .")
os.system("git commit -m 'add a new image'")
os.system("git push origin main")

for file in os.listdir("."):
    if file != "rename.py": os.system(file)

