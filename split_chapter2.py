filename = 'caged_bird_clean.txt'
count = -1
startCount = 0
chapter = 0
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    count = count + 1
    if line.find('CHAPTER')>0:
        print(line)
        wayBefore = count -3
        before = count -1
        after = count + 1
        wayAfter = count + 6
        print(lines[wayBefore])
        print(lines[before])
        print(lines[after])
        print(lines[wayAfter])
        print(lines[wayBefore:wayAfter])

    # if line[0:7] == "CHAPTER":
        # newFile = "chapter" + str(chapter)+ ".txt"
        # chapterList = lines[startCount:count]
        # f = open(newFile, 'w')
        # f.writelines(chapterList)
        # f.close()
        # startCount = count
        # chapter = chapter + 1
