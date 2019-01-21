l=[12,21,4,243,5,24,5325,324,23532,43,42,432,434,4,32532,523,5,7568,4,4,
78,9876,69,8]
l1=[]
l1.append(l[0])
l2=[]
l2.append(l[0])

# 比较排序
for i in range(1,len(l)):
    for y in range(0,len(l1)):
        arr = l[i]
        if arr <= l1[y]:
            l1.insert(y,l[i])
            break
        else:
            continue
    else:
        l1.append(l[i])
    
print(l1)

# 冒泡排序
for i in range(1,len(l)):
    arr = l[i]
    for y in range(0,len(l2)):
        if arr <= l2[y]:
            l2[y],arr = arr,l2[y]   
    else:
        l2.append(arr)
    
print(l2)


