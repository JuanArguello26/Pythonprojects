# Import the tkinter library, which is the standard Python interface for creating GUIs.
import tkinter as tk

# Create the main application window object.
# This 'root' window is the main container for all other GUI elements (widgets).
main_window = tk.Tk()

# Set the title that appears in the title bar of the window.
main_window.title("Simple GUI")

# Set the initial size of the window (width x height).
main_window.geometry("250x100")

# Create a Label widget.
# A label is a widget used to display a static piece of text.
# - The first argument 'main_window' tells the label which window it belongs to.
# - The 'text' parameter sets the text to be displayed.
greeting_label = tk.Label(main_window, text="Hello, World!")

# Use the pack() geometry manager to make the widget visible.
# This method organizes widgets in blocks before placing them in the parent widget.
# We add some padding on the x and y axes to give it some space.
greeting_label.pack(pady=20)

# Start the main event loop.
# This line is crucial; it keeps the window open and listens for events (like button clicks or closing the window)
# until the user closes it.
main_window.mainloop()