import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList

for i in ourList:
    if i>4:
        continue
    belowFive.append(i)
print(belowFive)
