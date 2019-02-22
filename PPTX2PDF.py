"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: Converting multiple PPT files to PDF.
 ********************************************/"""
import os,comtypes.client,sys

powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
powerpoint.Visible = 1

for file in sys.argv[1:]:
    flag = False

    currentPath = os.path.abspath(__file__)
    currentDir = os.path.dirname(currentPath)
    dirWithFileName = os.path.join(currentDir, file)  #creating the abs dir for the file

    if dirWithFileName[-4:] == 'pptx' or dirWithFileName[-3:] == 'ppt':
        powerpointWindow = powerpoint.Presentations.Open(dirWithFileName)

        powerpointWindow.SaveAs(dirWithFileName[:-4] + 'pdf'
                                if dirWithFileName[-4:] == 'pptx'
                                else dirWithFileName[:-3] + 'pdf', 32)  # add pdf, formatType = 32 for ppt to pdf

        powerpointWindow.Close()
        flag = True

    print("Success" if flag else ("Fail to convert " + file))

powerpoint.Quit()

"""Note:***********************************************************
        you can use pyinstaller to make an executable .exe file
        so you can drag and drop the ppt files into it's icon
        and the output pdf will appear next to it.
***************************************************************/"""
