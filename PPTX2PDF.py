"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: Converting multiple PPT files to PDF.
 ********************************************/"""
import os   
import sys
import comtypes.client

powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
powerpoint.Visible = 1

for file in sys.argv[1:]:
    x=0

    mypath = os.path.abspath(__file__)
    mydir = os.path.dirname(mypath)
    file_input = os.path.join(mydir, file) #creating the abs dir for the file

    if file_input[-4:]=='pptx' or file_input[-3:]=='ppt':
        deck = powerpoint.Presentations.Open(file_input)
        deck.SaveAs(file_input[:-4]+'pdf' if file_input[-4:]=='pptx' else file_input[-3:]+'pdf', 32) # add pdf,formatType = 32 for ppt to pdf
        deck.Close()
        x=1

    print ("Success\n" if x==1 else "Fail\n")

powerpoint.Quit()

"""Note:***********************************************************
        you can use pyinstaller to make an executable .exe file
        so you can drag and drop the ppt files into it's icon
        and the output pdf will appear next to it.
***************************************************************/"""
