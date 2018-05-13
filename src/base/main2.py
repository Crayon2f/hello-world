import datetime
import os
import uuid

string = '?dd'
print string.find('ff')
print string.replace('d', 'f')
print [1, 2, 3, 4][2:]

print uuid.uuid4()
print uuid.uuid4()
print uuid.uuid4()
print uuid.uuid4()
print str(uuid.uuid4())[:8]

var = [1, 2, 3, 5, 4]
print(0 in var)


print(os.path.exists("/Volumes/Crayon2f/artworks"))


for i in [1,2,3]:
    if i == 2:
        continue
    print(i)
