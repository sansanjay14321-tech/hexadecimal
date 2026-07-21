salary=int(input("salary:"))
age=int(input("age:"))
loan=int(input("loan:"))
if(salary>=20000 or age<=25):
    if(loan>50000):
        print("maximum loan for 50000")
    else:
        print("you are eligible")
else:
    print("you are not eligible for loan")
