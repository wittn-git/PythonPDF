from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from PIL import Image
from os.path import exists

def merge(doc_names, result_name):
    merger = PdfFileMerger()
    for pdf in doc_names:
        merger.append(pdf)
    if(exists(result_name)): raise Exception("Output file already exists")
    merger.write(result_name)
    merger.close()

def extract(doc_name, pages, result_name): 
    writer = PdfFileWriter()
    reader = PdfFileReader(doc_name)
    for page in pages:
        writer.addPage(reader.getPage(page-1))
    if(exists(result_name)): raise Exception("Output file already exists")
    with open(result_name,'wb') as out:
        writer.write(out)

def split(doc_name, page, result_names):
    reader = PdfFileReader(doc_name)
    ranges = ((0, page), (page+1, reader.getNumPages()))
    for i in range(2):
        writer = PdfFileWriter()
        for page in range(ranges[i][0], ranges[i][1]):
            writer.addPage(reader.getPage(page-1))
        if(exists(result_names[i])): raise Exception("Output file already exists")
        with open(result_names[i],'wb') as out:
            writer.write(out)

def convert_png(doc_name, result_name):
    img = Image.open(doc_name)
    img = img.convert('RGB')
    img.save(result_name)