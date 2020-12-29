filename = 'caged_bird_clean.txt'
count = -1
startCount = 0
chapter = 0
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    count = count + 1
    if line[0:7] == "CHAPTER" or line.find('CHAPTER')>0:
        newFile = "chapter" + str(chapter)+ ".txt"
        chapterList = lines[startCount:count]
        f = open(newFile, 'w')
        f.writelines(chapterList)
        f.close()
        startCount = count
        chapter = chapter + 1
