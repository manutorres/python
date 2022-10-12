import PyPDF2

with open("adidas.pdf", "rb") as file:  # Leer en modo binario
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["adidas.pdf", "rider.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("merged.pdf")
