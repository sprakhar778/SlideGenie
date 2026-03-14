from pypdf import PdfWriter

def merge_pdfs(output_name, pdf_list):
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_name)
    merger.close()
    print(f"Success! {output_name} created.")

# List your files here in order
files_to_merge = ["output.pdf", "output2.pdf","output1.pdf","output4.pdf"]
merge_pdfs("final_presentation.pdf", files_to_merge)