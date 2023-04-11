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
    num = (re.findall('[0-9]+', line))
    if len(num) >= 1:
        lst += num
    else:
        continue
        
lst = [int(num) for num in lst]

for num in lst:
    total += num
     
print(total)
