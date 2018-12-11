import sys
from PyPDF2 import PdfFileMerger, PdfFileReader
merge=PdfFileMerger()
x=0
for file in sys.argv[1:]:
    if file[-3:]=='pdf':
        with open(file, 'rb') as fpdf:
            merge.append(PdfFileReader(fpdf))
        x=1
    if x:
        merge.write("output.pdf")
print ("Success\n" if x==1 else "Fail\n")
