def fileOpen():
    while True:
        fName = input("Enter file name, or type 'Exit Program': ")
        if fName == 'Exit Program':
            quit()
        else:
            try:
                fHand = open(fName)
                return fHand, fName
            except:
                print('Invalid file name:', fName)

import re
fHand, fName = fileOpen()
lst = []
total = 0

for line in fHand:
    match = re.search('^New\sRevision:\s', line)
    if match != None:
        num = re.findall('[0-9]+', line)
        num = int(num[0])
        lst.append(num)
        total = total + num
    else:
        continue

average = int(total / len(lst))
print(average)
