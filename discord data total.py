from wordcloud import STOPWORDS
import string
stopwords = set(STOPWORDS)

with open(r'C:\Users\cland\Documents\GitHub\DiscordData\rotow - Text - osu [284065284241752065] thru 06112020.txt', encoding='utf8') as words1:
    words1 = words1.read()
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\rotow - Text - pit-of-unfortune [490245096491581450] thru 06112020.txt', encoding='utf8') as words2:
    words2 = words2.read()
words = words1+words2
words = words.replace("I'm",'').replace("Im",'').replace('im','').replace("i'm",'').replace("LINK HERE ","").replace('\n',' ').replace("link",'')
badchars = words.translate({ord(i): None for i in string.printable})
badchars += str([".,`[]()*"])
words = words.translate({ord(i): None for i in badchars})\
    .replace(r'Attachments','').replace(r'attachments','').replace(r'{}','')

def sortfreqdict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

wordlist = words.split()
wordlist = [w for w in wordlist if w not in stopwords]
wordfreq = [wordlist.count(w) for w in wordlist]

freqdict = dict(list(zip(wordlist, wordfreq)))
freqdict = sortfreqdict(freqdict)
filename = r"C:\Users\cland\Documents\GitHub\DiscordData\\" + "total_dictionary.txt"
indivdict = open(filename, "w")
indivdict.write(str(freqdict))
indivdict.close()