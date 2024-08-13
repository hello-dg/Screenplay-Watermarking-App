import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
from PyPDF2 import PdfReader, PdfWriter

# Global Variables
file_path = 'yes'


# Function to handle button click
def on_button_click():
    print("Button Works")


def upload_file():
    global file_path
    permitted_file_types = [("PDF files", '*.pdf')]
    file_path = filedialog.askopenfilename(filetypes=permitted_file_types)
    if file_path:
        print(f"File selected: {file_path}")


def generate_text_for_watermarking(text, font_size=36):
    font = ImageFont.truetype('arial.ttf', font_size)
    text_size = font_size
    background = Image.new('RGBA', text_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(background)
    draw.text((0, 0), text, font=font, fill=(0, 0, 0, 128))

    return background


# Create the main window
root = tk.Tk()
root.title("Watermark It!")
root.geometry('400x300')
root.config(bg='#fefefe')
root.iconbitmap('assets/icons/drop.ico')

# Create and pack the widgets
label = tk.Label(root, text="If you haven't already... Watermark It!", font=('Rockwell', 14), fg='#7393B3', bg='#fefefe')
label.pack(pady=10)

button = tk.Button(root, text="Upload PDF Document", font=('Rockwell', 12), fg="#ffffff", bg='#7393B3', command=upload_file)
button.pack(pady=10)

label = tk.Label(root, text="Watermark Text:", font=('Rockwell', 12), fg='#7393B3', bg='#fefefe')
label.pack(pady=10)

watermark_entry = tk.Entry(root)
watermark_entry.pack(pady=10)

button = tk.Button(root, text="Watermark It!", font=('Rockwell', 12), fg="#ffffff", bg='#7393B3', command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()