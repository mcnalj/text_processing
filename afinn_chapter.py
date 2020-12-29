"""This takes a chapter and identifies the
most emotionally charged sentences."""


from afinn import Afinn

afinn = Afinn(language='en')


def linesToCleanSentences(chapter):
    """ This takes a chapter in the form of a list of strings.
    It takes out the newline characters and returns the chapter
    as a list of sentences."""
    filename = chapter
    count = 0
    fullChapter = ""
    linesArray = []
    with open(filename) as file_object:
        lines = file_object.readlines()
    fullChapter = fullChapter.join(lines)
    chapterList = fullChapter.split(".")
    for line in chapterList:
        line = line.strip('\n')
        line = line.replace('\n', ' ')
        linesArray.append(line)
    return linesArray


filename = 'chapter23.txt'

fullChapter = ''
count = -1
strongPositive = 0
strongPositiveArray = []
strongNegative = 0
strongNegativeArray = []
totalScore = 0

# with open(filename) as file_object:
    # lines = file_object.readlines()
    # fullChapter = fullChapter.join(lines)
    # lines = fullChapter.split(".")

lines = linesToCleanSentences("chapter23.txt")

for line in lines:
    count = count + 1
    score = afinn.score(line)
    totalScore = totalScore + score
    line = line + '.'
    if score >= 5:
        strongPositive +=1
        index = line.find('\\n')
        if index > 0:
            length = len(line)
            lineA = line[0:index + 1]
            lineB = line[index+2:]
            line = lineA + lineB
        strongPositiveArray.append(line)
    if score <= -5:
        strongNegative +=1
        index = line.find('\n')
        if index>0:
            length = len(line)
            lineA = line[0:index + 1]
            lineB = line[index+2:]

        strongNegativeArray.append(line)
for pos in strongPositiveArray:
    print(pos)
for neg in strongNegativeArray:
    print(neg)
print("Strong Positive Count: " + str(strongPositive))
print("Strong Negative Count: " + str(strongNegative))
print("Total Chapter Score: " + str(totalScore))
avgLineScore = totalScore/count
print("Average line score: " + str(avgLineScore))
