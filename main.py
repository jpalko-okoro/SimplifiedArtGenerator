import tkinter as tk
import ImageGrid

if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    app = ImageGrid.ImageGridApp(root)  # Initialize the ImageGridApp class
    root.mainloop()  # Start the Tkinter event loop
