import tkinter as tk
import os
import ImageProcessing

from tkinter import filedialog
from PIL import Image, ImageTk


class ImageGridApp:

    def __init__(self, main):
        self.main = main
        main.title("Image Grid")

        screen_width = main.winfo_screenwidth()
        screen_height = main.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_position = (screen_width // 2 - main.winfo_reqwidth()) // 2
        y_position = (screen_height // 2 - main.winfo_reqheight()) // 2

        # Set the window position and size
        window_width = 650
        window_height = 700
        main.geometry("{}x{}+{}+{}".format(window_width, window_height,
                                           x_position, y_position))

        # To store references to ImageTk.PhotoImage objects
        self.image_refs = []

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
        initial_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = filedialog.askopenfilename(initialdir=initial_dir,
                                               filetypes=[("PNG files",
                                                           "*.png")])
        if file_path:
            self.show_image(
                file_path)  # If a file is selected, call the show_image method

    def maintain_aspect_ratio(self, image, new_width):
        width_percent = (new_width / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        return image.resize((new_width, new_height),
                            3)  # 3 corresponds to Image.ANTIALIAS

    # Method to clear the previous images and labels
    def clear_previous_images(self):
        for widget in self.image_frame.winfo_children():
            widget.destroy()

    # Method to display the selected image in a 2x2 grid
    def show_image(self, file_path):
        self.clear_previous_images()

        image = Image.open(file_path)

        # Define the desired width while maintaining aspect ratio (This should probably be done after the filtering is finished)
        desired_width = 250

        # Resize the image with the aspect ratio preserved
        image = self.maintain_aspect_ratio(image, desired_width)
        grayscale_image = image.convert('LA')
        filtered_image_pass_1 = ImageProcessing.image_filtering_pass_1(grayscale_image)

        for i in range(2):
            for j in range(2):
                if i == 0 and j == 1:
                    used_image = grayscale_image
                elif i == 1 and j == 0:
                    used_image = filtered_image_pass_1
                else:
                    used_image = image

                # Create a label to display the resolution of the image
                label = tk.Label(
                    self.image_frame,
                    text=
                    f"Resolution: {used_image.size[0]}x{used_image.size[1]}")
                label.grid(row=i, column=j)

                photo = ImageTk.PhotoImage(used_image)
                self.image_refs.append(
                    photo)  # Store the reference to prevent garbage collection

                image_label = tk.Label(self.image_frame, image=photo)
                image_label.used_image = photo
                image_label.grid(row=i, column=j)
