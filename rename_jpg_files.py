import os
path = os.getcwd()

i = 1
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() == ".jpg":
        new_file_name = "Image {}.jpg".format(i)
        os.rename(file, new_file_name)
        i = i + 1