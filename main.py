import tkinter as tk
from tkinter import filedialog, messagebox
from pdfrw import PdfReader, PdfWriter, PageMerge
# from PyPDF2 import PdfReader, PdfWriter

# Global Variables
file_path = 'assets/pdf/test.pdf'
watermark_text = 'assets/pdf/wmtest.pdf'
output = 'assets/pdf/endtest.pdf'


# Function to handle button click
def on_button_click():
    print("Button Works")


def upload_file():
    global file_path
    permitted_file_types = [("PDF files", '*.pdf')]
    file_path = filedialog.askopenfilename(filetypes=permitted_file_types)
    if file_path:
        print(f"File selected: {file_path}")


def get_watermark_entry():
    global watermark_text
    watermark_text = watermark_entry.get()
    print(watermark_text)


def get_pdf_info():
    global file_path
    pdf = PdfReader(file_path)

    print(pdf.Info)
    print(pdf.Root.keys())
    print('PDF has {} pages'.format(len(pdf.pages)))


def watermark_pdf():
    global file_path, watermark_text, output
    pdf = PdfReader(file_path)
    watermark = PdfReader(watermark_text)
    pages_to_mark = watermark.pages[0]

    for page in range(len(pdf.pages)):
        merger = PageMerge(pdf.pages[page])
        merger.add(pages_to_mark).render()

    writer = PdfWriter()
    writer.write(output, pdf)


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

watermark_entry = tk.Entry(root, font=('Rockwell', 12))
watermark_entry.pack(pady=10)

button = tk.Button(root, text="Watermark It!", font=('Rockwell', 12), fg="#ffffff", bg='#7393B3', command=watermark_pdf)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()