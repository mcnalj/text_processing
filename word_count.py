filename = 'caged_bird.txt'

wordsLists = []
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        words = line.split()
        wordsLists.append(words)
uniqueWords = [{'uniqueWord': "Maya", 'appearances': 0}]
for list in wordsLists:
    for word in list:
        toAppend = True
        for dict in uniqueWords:
            if dict['uniqueWord'] == word:
                dict['appearances'] = dict['appearances'] + 1
                toAppend = False
                break
        if toAppend:
            wordDict = {
                'uniqueWord': word,
                'appearances': 1
            }
            uniqueWords.append(wordDict)

print(sorted(uniqueWords, key = lambda item: item['appearances']))
