# given a list of voter , check whether there is any voter with target age using while loop

targetAge=50
age_list1=[51,20,70,90,21]
age_list2=[47,29,50,67,32]


idx=0
n=len(age_list1)
found=False

while idx<n:
    if age_list2[idx]==targetAge:
        found=True
        idx+=1
        break
    else:
        idx+=1

if found==True:
    print("voter exist with target age")
else:
    print("voter list does not exist with target list")