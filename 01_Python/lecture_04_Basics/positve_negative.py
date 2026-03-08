#example of even/odd + positive/negative


number = int(input("Enter a number :"))
if number >0:
    print("Number is positive")
    if number % 2 ==0:
        print("Number is even")
    else: 
        print("Number is odd")
else:
    print("Number is zero or negative")

