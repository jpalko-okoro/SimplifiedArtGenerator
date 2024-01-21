# Image Grid Generator
This Python script creates a simple graphical user interface (GUI) for generating a 2x2 grid of images from selected PNG files. The images are displayed in the grid, and each image is accompanied by a label showing its resolution. The script uses the Tkinter library for GUI creation and the Pillow library (PIL) for image processing.

## Usage
### Run the Script:
1. Execute the script, and a GUI window will appear.
2. Select PNG File:
Click the "Open PNG File" button, and a file dialog will appear.
Choose a PNG file from the dialog.
3. Review Image Grid:
After selecting a PNG file, the script will display the image in a 2x2 grid format within the GUI.
Each image is accompanied by a label indicating its resolution.

## Maintain Aspect Ratio

The script maintains the aspect ratio when resizing the images to fit into the grid.

## Requirements
* Python 3.9.x (Tested with this version, but may work with other Python 3 versions)
* tkinter library (Included in most Python installations)
* Pillow library (Install with `pip install Pillow`)

## Notes
The script is designed to work with PNG files, and it maintains the aspect ratio when displaying images in the grid.
Adjust the desired width for resizing images in the script if needed.
Feel free to explore and experiment with different PNG files to see them displayed in the 2x2 grid within the GUI.


