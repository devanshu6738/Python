arr=[1,2,3,4,5]
print(len(arr))
def SumOfArray(arr,N):
    if N==0:
        return 0
    return arr[N-1]+SumOfArray(arr,N-1)

print(SumOfArray(arr,5))
print(arr[4])