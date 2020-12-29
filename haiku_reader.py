#with open('haiku.txt') as file_object:
#    contents = file_object.read()

filename = 'caged_download_clean.txt'
searching = True
while searching:
    wordsLists = []
    count = 0
    wordToCount = input("Enter the word you want to count: ")
    if wordToCount == 'q':
        print("Thanks for playing!")
        searching = False
    else:
        with open(filename) as file_object:
            lines = file_object.readlines()
            for line in lines:
                words = line.split()
                wordsLists.append(words)
                for word in words:
                    if word.lower() == wordToCount:
                        count = count+1
        count = str(count)
        print(f"The word {wordToCount} appears {count} times in the haiku.")




#wordsLists = []
#with open('haiku.txt') as file_object:
#    lines = file_object.readlines()
#    for line in lines:
#        words = line.split()
#        wordsLists.append(words)
#        print(len(words))
#print(wordsLists)
