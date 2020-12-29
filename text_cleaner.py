filename = 'caged_bird.txt'
count = -1
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    count = count + 1
    if line[2:10] == "KNOW WHY":
        del lines[count]
    if line[3:11] == "KNOW WHY":
        del lines[count]
    if line[1:9] == "KNOW WHY":
        del lines[count]
    if line[2:10] == "MAYA ANG":
        print("first: " +lines[count])
        del lines[count]
    if line[3:11] == "MAYA ANG":
        print("second: " + lines[count])
        del lines[count]
    if line[4:12] == "MAYA ANG":
        print("third: " + lines[count])
        del lines[count]
    if line[5:13] == "MAYA ANG":
        print("fourth: " + lines[count])
        del lines[count]


f = open('caged_bird_clean.txt', 'w')
f.writelines(lines)
f.close()
