import numpy as np
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import string
  
filepath = r'C:\Users\cland\Documents\GitHub\DiscordData\will_individual.txt'
with open(filepath, 'r', encoding='utf8') as words:
    words = words.read().replace("LINK HERE ","").replace('\n',' ')
badchars = words.translate({ord(i): None for i in string.printable})
badchars += str([".,`[]()*"])
words = words.translate({ord(i): None for i in badchars})\
    .replace(r'Attachments','').replace(r'attachments','').replace(r'{}','')
#print(words)

x, y = np.ogrid[:1000, :1000]

mask = (x - 500) ** 2 + (y - 500) ** 2 > 500 ** 2
mask = 255 * mask.astype(int)


wc = WordCloud(background_color="white", repeat=True, mask=mask, collocations=False,\
    height=1000, width=1000)
wc.generate(words)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()