with open(r"C:\Users\cland\Documents\GitHub\DiscordData\test.txt", "r", encoding="utf8") as test:
    lines = list(line for line in (l.strip() for l in test) if line)
idnum = "#0296"

for idx, elem in enumerate(lines):
    thiselem = elem
    nextelem = lines[(idx + 1) % len(lines)]
    if idnum in lines[idx]:
        print(nextelem)