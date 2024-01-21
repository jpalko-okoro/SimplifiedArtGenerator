import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Class definition for the ImageGridApp
class ImageGridApp:

    def __init__(self, main):
        # Initialization method for the class
        self.main = main
        main.title("Image Grid")  # Set the title of the Tkinter window

        # Calculate the screen width and height
        screen_width = main.winfo_screenwidth()
        screen_height = main.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_position = (3 * screen_width // 4 - main.winfo_reqwidth()) // 2
        y_position = (3 * screen_height // 4 - main.winfo_reqheight()) // 2

        # Set the window position
        main.geometry("+{}+{}".format(x_position, y_position))

        self.image_refs = [
        ]  # To store references to ImageTk.PhotoImage objects

        # Create a frame to hold the left-hand column and image grid
        main_frame = tk.Frame(main)
        main_frame.pack()

        # Create a left-hand column to hold the "Open PNG File" button
        left_column = tk.Frame(main_frame)
        left_column.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

        # Create a button to open the file dialog
        open_button = tk.Button(left_column,
                                text="Open PNG File",
                                command=self.open_file_dialog)
        open_button.pack(side=tk.TOP, anchor=tk.NW)

        self.image_frame = tk.Frame(main_frame)
        self.image_frame.grid(
            row=0, column=1)  # Create a frame to hold the image grid

    def open_file_dialog(self):
        # Method to open a file dialog for selecting a PNG file
        initial_dir = get_script_directory()
        file_path = filedialog.askopenfilename(initialdir=initial_dir,
                                               filetypes=[("PNG files",
                                                           "*.png")])
        if file_path:
            self.show_image(
                file_path)  # If a file is selected, call the show_image method

    def maintain_aspect_ratio(self, image, new_width):
        # Method to resize the image while maintaining aspect ratio
        width_percent = (new_width / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        return image.resize((new_width, new_height),
                            3)  # 3 corresponds to Image.ANTIALIAS

    def show_image(self, file_path):
        # Method to display the selected image in a 2x2 grid
        image = Image.open(file_path)

        # Define the desired width while maintaining aspect ratio
        desired_width = 200

        # Resize the image with the aspect ratio preserved
        image = self.maintain_aspect_ratio(image, desired_width)

        for i in range(2):
            for j in range(2):
                # Create a label to display the resolution of the image
                label = tk.Label(
                    self.image_frame,
                    text=f"Resolution: {image.size[0]}x{image.size[1]}")
                label.grid(row=i, column=j)  # Grid layout for the labels

                photo = ImageTk.PhotoImage(image)
                self.image_refs.append(
                    photo)  # Store the reference to prevent garbage collection

                # Create a label to display the image
                image_label = tk.Label(self.image_frame, image=photo)
                image_label.image = photo
                image_label.grid(row=i, column=j)  # Grid layout for the images


# Function to get the directory of the script
def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = ImageGridApp(root)  # Initialize the ImageGridApp class
    root.mainloop()  # Start the Tkinter event loop
