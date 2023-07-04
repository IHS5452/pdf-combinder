from PyPDF2 import PdfMerger

def combine_pdfs():
    merger = PdfMerger()
    file_number = 1

    while True:
        file_path = input(f"Enter path for PDF #{file_number} (or 'done' to finish): ")
        if file_path.lower() == "done":
            break

        try:
            merger.append(file_path)
            print(f"PDF #{file_number} added successfully.")
            file_number += 1
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")

    output_filename = 'combined.pdf'
    merger.write(output_filename)
    merger.close()

    print('PDF files combined successfully into', output_filename)

combine_pdfs()
