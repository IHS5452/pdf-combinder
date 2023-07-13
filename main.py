from PyPDF2 import PdfMerger

def combine_pdfs():
    merger = PdfMerger()
    file_number = 1

    save_location = input("Enter the save location: ")
    output_filename = input("Enter the output file name: ")
    output_filepath = f"{save_location}/{output_filename}"

    while True:
        file_path = input(f"Enter path for PDF #{file_number} (or 'done' to finish): ")
        if file_path.lower() == "done":
            break

        # Strip quotes from the file path
        file_path = file_path.strip('\'"')

        try:
            merger.append(file_path)
            print(f"PDF #{file_number} added successfully.")
            file_number += 1
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")

    merger.write(output_filepath)
    merger.close()

    print('PDF files combined successfully. Output file:', output_filepath)

combine_pdfs()
