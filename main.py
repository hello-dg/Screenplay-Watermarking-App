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


def watermark_pdf():
    global pdf_upload
    global pdf_download
    watermark = 'watermark.pdf'

    with open(pdf_upload, 'rb') as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfReader(input_file)
        watermark_pdf = PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]

        output = PdfWriter()

        for i in range(len(input_pdf.pages)):
            pdf_page = input_pdf.pages[i]
            pdf_page.merge_page(watermark_page)
            output.add_page(pdf_page)

        with open(pdf_download, 'wb') as merged_file:
            output.write(merged_file)


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