import time, copy, sys

testcase1 = [[12, 55, 67], [4, 71, 59], [20, 67, 70], [92, 68, 90], [83, 54, 13]]

def LRJF(works):
    start_time = time.time()
    output = copy.deepcopy(works)
    quickSort(output, 0, len(works)-1, 2)
    print("LRJF runtime = %s seconds" % (time.time() - start_time))
    return output
def FCFS(works):
    start_time = time.time()
    output = copy.deepcopy(works)
    quickSort(works, 0, len(works)-1, 0)
    print("FCFS runtime = %s seconds" % (time.time() - start_time))
    return output

def quickSort(m, first, last, vtc):
    if first < last:
        splitpoint = partition(m, first,last, vtc)
        quickSort(m, first, splitpoint-1, vtc)
        quickSort(m, splitpoint+1, last, vtc)

def partition(m, first, last, vtc):
   pivotvalue = m[first][vtc]
   leftmark = first + 1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and m[leftmark][vtc] <= pivotvalue:
           leftmark = leftmark + 1
       while m[rightmark][vtc] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark - 1
       if rightmark < leftmark:
           done = True
       else:
           temp = m[leftmark]
           m[leftmark] = m[rightmark]
           m[rightmark] = temp
   temp = m[first]
   m[first] = m[rightmark]
   m[rightmark] = temp

   return rightmark

def totalTime(m):
    output = []
    for i, col in enumerate(m):
        sum = col[0] + col[2]
        for j in range(i+1):
            sum += m[j][1]
        output.append(sum)
    return(output)



out = LRJF(testcase1)

for i in range(3):
    for col in out:
        print(col[i], end="\t")
    print("\n")

print("Total time cost of each branch: ")
for n in totalTime(out):
    print(n, end = "\t")
print("\n")

