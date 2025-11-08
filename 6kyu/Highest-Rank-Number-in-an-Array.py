# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.

# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

from collections import Counter


def highest_rank(arr):
    objArr ={}

    for i in arr:
        if i in objArr:
            objArr[i]+=1
        else:
            objArr[i] = 1


    sortedArr = sorted(list(objArr.values()), reverse=True)

    highest = sortedArr[0]

    result = []

    for key,value in objArr.items():
        if value == highest:
            result.append(key)
    
    if len(result)==1:
        print(result[0])
    else:
        highestResult = sorted(result, reverse=True)
        print(highestResult[0])

########################################
# or
# from collections import Counter
    # counts = Counter(arr)
    # maxValues = max(counts.values())

    # return max(k for k,v in counts.items() if v == maxValues) //Here we get all the value instances equal to maxValuesand get the greater one with max
########################################
# or
    # return  max(sorted(arr,reverse=True), key = arr.count)


highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10])