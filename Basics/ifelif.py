#write a program that takes age as a input and tell whether a person is eligible to vote or not.

age=int(input("Enter ur age"))

if age>=18:
    print("U r eligible to vote")
elif age<=0:
    print("Error in the age")
else:
    print("Sorry! u r not eligible")