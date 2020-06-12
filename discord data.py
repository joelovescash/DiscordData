from wordcloud import STOPWORDS
stopwords = set(STOPWORDS)

idnum = "#0296"     # Wills number ID    
name = "will" 
import os.path, string
from os import path
filepath = r"C:\Users\cland\Documents\GitHub\DiscordData\\" + name + "_individual.txt"
#print(filepath)
#print(path.exists(filepath))

with open(r"C:\Users\cland\Documents\GitHub\DiscordData\rotow - Text - pit-of-unfortune [490245096491581450] thru 06112020.txt", encoding="utf8") as chatlog:
    lines = list(line for line in (l.strip() for l in chatlog) if line)

individual = open(filepath, "w", encoding="utf8")
for idx, elem in enumerate(lines):
    thiselem = elem
    nextelem = lines[(idx + 1) % len(lines)]
    if idnum in lines[idx]:
        if "http" in lines[idx+1]:
            individual.write("LINK HERE ")
        else:
            individual.writelines([nextelem, "\n"])
individual.close()

with open(filepath, 'r', encoding='utf8') as individual:
    individual = individual.read().lower().replace("LINK HERE ","").replace('\n',' ')
badchars = individual.translate({ord(i): None for i in string.printable})
badchars += str([".,`[]()*"])
#print(type(badchars))
#print(badchars)
individual = individual.translate({ord(i): None for i in badchars})\
    .replace(r'Attachments','').replace(r'attachments','').replace(r'{}','')

def sortfreqdict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

wordlist = individual.split()
wordlist = [w for w in wordlist if w not in stopwords]
wordfreq = [wordlist.count(w) for w in wordlist]

freqdict = dict(list(zip(wordlist, wordfreq)))
freqdict = sortfreqdict(freqdict)
filename2 = r"C:\Users\cland\Documents\GitHub\DiscordData\\" + name + "_dictionary.txt"
indivdict = open(filename2, "w")
indivdict.write(str(freqdict))
indivdict.close()