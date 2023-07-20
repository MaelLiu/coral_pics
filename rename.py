import os
for file in os.listdir("."):
    if '.' not in file:
        new_file = file + ".png"
        os.rename(file, new_file)
        os.system("git add .")
        os.system("git commit -m 'add a new image'")
        os.system("git push origin main")
        print(new_file)
        os.system("rm {new_file}")

