from afinn import Afinn

afinn = Afinn(language='en')

chaptersList = []
chapterCount = 0

while chapterCount<36:
    fullChapter = ''
    filename = 'chapter' + str(chapterCount) +'.txt'

    count = -1
    strongPositive = 0
    strongPositiveArray = []
    strongNegative = 0
    strongNegativeArray = []
    totalScore = 0

    with open(filename) as file_object:
        lines = file_object.readlines()
        fullChapter = fullChapter.join(lines)
        lines = fullChapter.split(".")

    for line in lines:
        count = count + 1
        score = afinn.score(line)
        totalScore = totalScore + score
        if score >= 3:
            strongPositive +=1
            strongPositiveArray.append(line)
        if score <= -3:
            strongNegative +=1
            strongNegativeArray.append(line)
    # print(strongPositive)
    # print(strongPositiveArray)
    # print(strongNegative)
    # print(strongNegativeArray)
    # print("Strong Positive Count: " + str(strongPositive))
    # print("Strong Negative Count: " + str(strongNegative))
    # print("Total Chapter Score: " + str(totalScore))
    avgLineScore = totalScore/count
    # print("Average line score: " + str(avgLineScore))
    chapter = {
        'chapter': chapterCount,
        'totalScore': totalScore,
        'avgLineScore': avgLineScore,
        'strongPositive': strongPositive,
        'strongNegative': strongNegative
    }
    chaptersList.append(chapter)
    chapterCount = chapterCount + 1

highest = 0
lowest = 0
lowestAvg = 0
highestAvg = 0
for chap in chaptersList:
    if chap["totalScore"] > highest:
        highestChapter = chap["chapter"]
        highest = chap["totalScore"]
    if chap["totalScore"] < lowest:
        lowestChapter = chap["chapter"]
        lowest = chap["totalScore"]
    if chap["avgLineScore"] > highestAvg:
        highestAvgChapter = chap["chapter"]
        highestAvg = chap["avgLineScore"]
    if chap["avgLineScore"] < lowestAvg:
        lowestAvgChapter = chap["chapter"]
        lowestAvg = chap["avgLineScore"]

print("Highest Chapter: " + str(highestChapter) + ': ' + str(highest))
print("Highest Chapter Average: " + str(highestAvgChapter) + ': ' + str(highestAvg))

print("Lowest Chapter: " + str(lowestChapter) + ': ' + str(lowest))
print("Lowest Chapter: " + str(lowestAvgChapter) + ': ' + str(lowestAvg))

for c in chaptersList:
    print(c)
    print('\n')
