import os
# path = os.chdir("C:\\Users\\Mohsin\\Desktop\\New folder - Copy (5)")

current_path = os.getcwd()

i = 1
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() == ".png":
        new_file_name = "Image {}.jpg".format(i)
        os.rename(file, new_file_name)
        i = i + 1