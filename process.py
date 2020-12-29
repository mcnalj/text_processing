filename = 'haiku.txt'
count = 0
linesArray = []
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    count = count + 1
    if count > 125 and count < 12000:
        lineArray = line.split()
        linesArray.append(lineArray)

longestWordValue = 0
longestWord = ''
churchCount = 0
whiteCount = 0
mamaCount = 0
testCount = 0
wordCount = 0
for line in linesArray:
    for word in line:
        wordCount = wordCount + 1
        if len(word)>longestWordValue:
            longestWord = word
            longestWordValue = len(word)
        if word == 'church':
            churchCount = churchCount + 1
        if word == 'white':
            whiteCount = whiteCount + 1
        if word.lower() == 'mama':
            mamaCount = mamaCount + 1
        if word == "I":
            testCount = testCount + 1
print(longestWord)
print(str(longestWordValue))
print(str(count))
print(churchCount)
print(whiteCount)
print(mamaCount)
print("Test: " + str(testCount))
print("word count: " + str(wordCount))
