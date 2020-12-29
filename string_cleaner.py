filename = 'haiku.txt'
count = 0
linesArray = []
cleanedLines = []
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = '\n'+ line
    linesArray.append(line)
for l in linesArray:
    l = l.strip('\n')
    cleanedLines.append(l)
print(cleanedLines)
