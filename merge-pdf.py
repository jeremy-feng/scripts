from PyPDF2 import PdfMerger

pdfs = ["./中文简历/冯超-简历.pdf", "./英文简历/Chao Feng-Resume.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(open(pdf, "rb"))

with open("冯超-简历.pdf", "wb") as fout:
    merger.write(fout)
