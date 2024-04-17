
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

for i in range (1,11):
   fact(i)
   print ( f"factorial of {i} is:{fact(i)}")












