# Image Renamer

This project provides a simple Python script and corresponding `.exe` files to rename all `.jpg` or `.png` images in a folder sequentially. The script is designed to be easy to use, and the `.exe` files allow you to run the renaming tool without needing Python installed on your system.

## Features

- Renames all `.jpg` or `.png` images in a folder to a sequential format (e.g., `Image 1.jpg`, `Image 2.jpg`, etc.).
- Comes with pre-built `.exe` files for easy execution.
- Lightweight and easy to use.

## How to Use

1. **Download the `.exe` file**:
   - For `.jpg` images: Download `rename_jpg.exe`.
   - For `.png` images: Download `rename_png.exe`.

2. **Place the `.exe` file**:
   - Move the downloaded `.exe` file into the folder containing the images you want to rename.

3. **Run the `.exe` file**:
   - Double-click the `.exe` file to execute it.
   - All `.jpg` or `.png` images in the folder will be renamed sequentially.

4. **Check the results**:
   - After execution, your images will be renamed in the format `Image 1.jpg`, `Image 2.jpg`, etc. (or `Image 1.png`, `Image 2.png`, etc. for PNG files).

## Python Script

If you prefer to use the Python script directly, follow these steps:

1. **Install Python**:
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Download the script**:
   - Save the script below as `rename_images.py`.

```python
import os

path = os.getcwd()

i = 1
for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() == ".jpg":  # Change to ".png" for PNG files
        new_file_name = "Image {}.jpg".format(i)  # Change to ".png" for PNG files
        os.rename(file, new_file_name)
        i = i + 1

```

3. **Run the script**:
   - Place the script in the folder containing your images.
   - Open a terminal or command prompt in that folder.
   - Run the script using the command:
     ```bash
     python rename_images.py
     ```

## Building the `.exe` File

If you want to build the `.exe` file yourself, follow these steps:

1. **Install PyInstaller**:
   - Install PyInstaller using pip:
     ```bash
     pip install pyinstaller
     ```

2. **Build the `.exe`**:
   - Navigate to the folder containing the script.
   - Run the following command to build the `.exe`:
     ```bash
     pyinstaller --onefile rename_images.py
     ```
   - The `.exe` file will be located in the `dist` folder.

## Notes

- The script only renames `.jpg` or `.png` files. Modify the script if you need to rename other file types.
- Always back up your images before running the script or `.exe` file to avoid accidental data loss.
- The script renames files in the order they are listed by the operating system, which may not always be alphabetical.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Feel free to contribute to this project or report issues on GitHub!