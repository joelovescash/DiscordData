from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import string
#name = "nate"
  
#filepath = r'C:\Users\cland\Documents\GitHub\DiscordData\\' + name + '_individual.txt'
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\will_individual.txt', encoding='utf8') as words1:
    words1 = words1.read()
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\bob_individual.txt', encoding='utf8') as words2:
    words2 = words2.read()
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\dylan_individual.txt', encoding='utf8') as words3:
    words3 = words3.read()
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\chris_individual.txt', encoding='utf8') as words4:
    words4 = words4.read()
with open(r'C:\Users\cland\Documents\GitHub\DiscordData\nate_individual.txt', encoding='utf8') as words5:
    words5 = words5.read()
words = words1+words2+words3+words4+words5
words = words.replace("I'm",'').replace("Im",'').replace('im','').replace("i'm",'').replace("LINK HERE ","").replace('\n',' ')
badchars = words.translate({ord(i): None for i in string.printable})
badchars += str([".,`[]()*"])
words = words.translate({ord(i): None for i in badchars})\
    .replace(r'Attachments','').replace(r'attachments','').replace(r'{}','')
#print(words)

wc = WordCloud(background_color="white", repeat=False, collocations=False,\
    height=1000, width=1000, min_font_size=12)
wc.generate(words)
plt.imshow(wc, interpolation="bilinear") 
plt.axis("off")  
plt.margins(x=0, y=0)
plt.show()