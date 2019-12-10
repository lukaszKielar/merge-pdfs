from PyPDF2 import PdfFileMerger
from tkinter import filedialog, messagebox
from os.path import dirname

__version__ = "0.0.2"

answer = True
initial_dir = "/"

while answer:

    pdfs = filedialog.askopenfilenames(
        initialdir=initial_dir,
        title="Select files",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
    )

    if len(pdfs) > 0:

        save_dir = dirname(pdfs[0])
        initial_dir = save_dir
        merger = PdfFileMerger()

        # iterate over pdfs
        for pdf in pdfs:
            print(pdf)
            merger.append(open(pdf, 'rb'))

        # select output path
        out_pdf = ""

        while out_pdf == "":
            out_pdf = filedialog.asksaveasfilename(
                initialdir=save_dir,
                defaultextension=".pdf",
                title="Select output location",
                filetypes=(("pdf files", "*.pdf"), ("all files", "*.*"))
            )
        # save new pdf in selected location
        with open(out_pdf, 'wb') as fout:
            merger.write(fout)

        messagebox.showinfo("Info", "File was saved in following directory\n{}".format(out_pdf))

    else:
        messagebox.showerror("Error!", "No files were specified!")

    answer = messagebox.askyesno("Continue?", "Do you want to run tool again?")
