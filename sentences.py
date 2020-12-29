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
