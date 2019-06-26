"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: scraping file extansion data from web and create a csv file
 ********************************************/"""
import pandas as pd
import requests
from bs4 import BeautifulSoup


def webScrapeTablesToLists(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0] 
    df = pd.read_html(str(table))[0].transpose()
    ls = df.iloc[0].str.lower()
    return ls.tolist()

def webScrapeTagsToDict(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content,'lxml')
    div = soup.find('div', attrs={'class': 'category'})
    dictLinks={}
    
    for aTag in div.find_all('a'):
        dictLinks.update({aTag.text : 'https://fileinfo.com'+aTag['href']})
    return dictLinks

links = webScrapeTagsToDict('https://fileinfo.com/browse/')

dataDict = {name:webScrapeTablesToLists(link) for (name,link) in links.items() if name != 'Common File Types'}

df = pd.DataFrame.from_dict(dataDict,orient='index').transpose()
df = df[~pd.isnull(df).all(1)].fillna('')
print(df)

df.to_csv('FileExtansionsDataSet.csv', index=False)
