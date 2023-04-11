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
regex = input('Enter a regular expression: ')
di = {}
lst = []

for line in fHand:
    if re.search(regex, line):
        di[regex] = di.get(regex, 0) + 1

for (k, v) in di.items():
    tup = (k, v)
    lst.append(tup)

for set in lst:
    print(fName, 'had', set[1], 'lines that matched', regex)
