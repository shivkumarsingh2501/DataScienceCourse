age = int(input("Enter age :"))
student = input("Aare you a student(yes/no): ")

if age <5:
    price = 0
elif age<12:
    price = 10

elif age <18:
    if student == "yes":
        price =12
    else:
        price =15
else:
    price =20

print( "Ticket price:", price )                        