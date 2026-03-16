# given a list of voter , check whether there is any voter with target age

targetAge=50
age_list1=[51,20,70,90,21]
age_list2=[47,29,50,67,32]

found=False

for i in age_list1:
    if(i==targetAge):
        found=True

if found==True:
    print("voter exist with target age")
else:
    print("voter list does not exist with target list")