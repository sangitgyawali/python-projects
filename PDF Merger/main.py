from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

print("===== PDF MERGER =====")

num_files = int(input("How many PDF files do you want to merge? "))

for i in range(num_files):
    pdf = input(f"Enter path of PDF {i + 1}: ")

    if os.path.exists(pdf):
        merger.append(pdf)
    else:
        print(f"File not found: {pdf}")

output = input("Enter output file name (e.g. merged.pdf): ")

merger.write(output)
merger.close()

print(f"\nPDFs merged successfully into '{output}'")