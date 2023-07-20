import os
for file in os.listdir("."):
    if '.' not in file:
        os.rename(file, file+".png")
        print(file + " is renamed")