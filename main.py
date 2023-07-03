import os
from PyPDF2 import PdfFileMerger

def combine_pdfs(directory):
    pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]
    pdf_files.sort(key=lambda x: int(x.split('.')[0]))

    merger = PdfFileMerger()

    for file in pdf_files:
        filepath = os.path.join(directory, file)
        merger.append(filepath)

    output_filename = 'combined.pdf'
    merger.write(output_filename)
    merger.close()

    print('PDF files combined successfully into', output_filename)

directory_path = 'PATH/TO/SAVE/COMBINDED/FILE'

combine_pdfs(directory_path)
