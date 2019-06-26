"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: organize the junk files in download folder
 ********************************************/"""
import os
import pandas as pd

fileExtansions = pd.read_csv('FileExtansionsDataSet.csv')
fileFormats = {fileExtansions[column].name: [y for y in fileExtansions[column] if not pd.isna(y)] for column in fileExtansions} #dict comprehension (dict of lists) for dataframe with drop for each nan value.
fileFormatsReversed = {file_format: folder for folder, fileFormat in fileFormats.items()  for file_format in fileFormat} #reversing key and value in list for future uses

def doTheJob():
    for file in os.scandir():
        print(file.path)
        if file.is_dir():
            continue
        fileFormat = os.path.splitext(file)[1]
        if fileFormat in fileFormatsReversed:
            if not os.path.exists(fileFormatsReversed[fileFormat]):
                os.makedirs(fileFormatsReversed[fileFormat])
            os.rename(file.path, os.path.join(os.getcwd(),fileFormatsReversed[fileFormat],file.name))
    

if __name__ == "__main__": 
    doTheJob() 