#  Write a program that check the number is prime or not
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
         return False
    return True

print(is_prime(4))
    
