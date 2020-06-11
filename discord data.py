with open(r"C:\Users\cland\Documents\GitHub\DiscordData\rotow - Text - pit-of-unfortune [490245096491581450] thru 06112020.txt", encoding="utf8") as chatlog:
    lines = list(line for line in (l.strip() for l in chatlog) if line)
individual = open(r"C:\Users\cland\Documents\GitHub\DiscordData\individual.txt", "w", encoding="utf8")
idnum = "#0296"     # Wills number ID     

for idx, elem in enumerate(lines):
    thiselem = elem
    nextelem = lines[(idx + 1) % len(lines)]
    if idnum in lines[idx]:
        if "http" in lines[idx+1]:
            individual.write("LINK HERE ")
        else:
            individual.writelines([nextelem, "\n"])
individual.close()