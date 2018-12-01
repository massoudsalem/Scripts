"""/*******************************************
 * - Coded by Moh.Massoud
 * - Problem: filtering old bookmarks or websites
 ********************************************/"""
import subprocess
import os
f=open("works1.txt", "a+")
FNULL = open(os.devnull, 'w')    #suppress subprocess output to devnull
with open('filename.txt') as fp:
    for line in fp:
        url=line.split()[1] #my list was having a number and then the url u can remove index if you don't
        res = subprocess.call(['ping', '-n', '1', url] , stdout=FNULL, stderr=subprocess.STDOUT)
        if res == 0: #if ping sucess save url to the other file
            f.write(url+"\n")
            print(url+"\n")
