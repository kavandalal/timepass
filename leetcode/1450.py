#1450

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4


c=0
for i in range(len(startTime)):
    if startTime[i]<=queryTime and endTime[i]>=queryTime:
        c+=1
print(c)