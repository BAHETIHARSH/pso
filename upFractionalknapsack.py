arr = [[60, 10], [100, 20], [120, 30]]
wt = 50
for i in range(len(arr)):
    arr[i].append(arr[i][1]/arr[i][0])
    
arr.sort(key = lambda temp:temp[2],reverse = True)

print(arr)
profit = 0
for item in arr:
    if item[1]<wt:
        profit += item[0]
        wt-=item[1]
    else:
        fraction = wt/item[1]
        profit += fraction*item[0]
        wt = 0 
print(profit)