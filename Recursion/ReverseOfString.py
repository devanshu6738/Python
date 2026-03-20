arr="Devanshu"

def ReverseOfString(arr,N):
    if N==0:
        return ""
    return arr[N-1]+ReverseOfString(arr,N-1) 

print(ReverseOfString(arr,8))

# done
