"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: Merging multiple pdf files togrther into single one
 ********************************************/"""
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
"""Note:***********************************************************
        you can use pyinstaller to make an excutable .exe file
        so you can drag and drop the pdf files into it's icon
        and the output pdf will appear next to itself.
***************************************************************/"""
