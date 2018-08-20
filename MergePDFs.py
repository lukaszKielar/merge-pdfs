# -.- encoding utf-8 -.-

__version__ = "0.0.1"

from PyPDF2 import PdfFileMerger
from tkinter import filedialog, messagebox
from os.path import dirname


pdfs = filedialog.askopenfilenames(initialdir="/", title="Select files", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
save_dir = dirname(pdfs[0])

merger = PdfFileMerger()

# iterate over pdfs
for pdf in pdfs:
    print(pdf)
    merger.append(open(pdf, 'rb'))

if len(pdfs) > 0:

    # select output path
    out_pdf = filedialog.asksaveasfilename(initialdir=save_dir, defaultextension=".pdf", title="Select output location", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))

    # save new pdf in selected location
    with open(out_pdf, 'wb') as fout:
        merger.write(fout)

    messagebox.showinfo("Info", "File was saved in following directory\n{}".format(out_pdf))

else:
    messagebox.showerror("Error!", "No files were specified!")



