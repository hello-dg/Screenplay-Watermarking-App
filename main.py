import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
import os

# Global Variables
pdf_upload = 'assets/pdf/test.pdf'
downloads_folder = os.path.expanduser('~/Downloads')
pdf_download = os.path.join(downloads_folder, 'Watermarked_File.pdf')


# Functions
def upload_file():
    global pdf_upload
    permitted_file_types = [("PDF files", '*.pdf')]
    pdf_upload = filedialog.askopenfilename(filetypes=permitted_file_types)
    if pdf_upload:
        print(f"File selected: {pdf_upload}")


def create_watermark():
    text = watermark_entry.get()
    pdf = canvas.Canvas('watermark.pdf', pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.gainsboro, alpha=0.6)
    pdf.setFont('Helvetica', 50)
    pdf.rotate(45)
    pdf.drawCentredString(400, 100, text)
    pdf.save()
    watermark_pdf()


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

button = tk.Button(root, text="Watermark It!", font=('Rockwell', 12), fg="#ffffff", bg='#7393B3', command=create_watermark)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()