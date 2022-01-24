import os
D={2000:0,500:0,200:0,100:0}
t=0
def admin():
    os.system('cls')
    global t
    while True:
        print("Welcome to admin page:)")
        a=input("Enter your username : ")
        b=input("Enter pin : ")
        if a=="Admin" and b=="12345":
            print("Logged in succesfully:)")
            while True:
                os.system('cls')
                print("1.Load")
                print("2.Balance Check")
                print("3.Exit")
                c=int(input("Enter your choice : "))
                os.system('cls')
                if(c==1):
                    for i in D:
                        print("Enter the number of",i,"notes : ")
                        e=int(input())
                        D[i]+=e
                        t=t+e*i
                elif(c==2):
                    for i in D:
                        print(i,"-",D[i])
                    print("Total amount is loaded:",t)
                elif(c==3):
                    return
                else:
                    print("Enter the correct option")
                
        else:
            print("Ivalid password")
def user():
    os.system('cls')
    global t,bal
    print("Welcome to user page:)")
    a=input("Enter pin : ")
    if a=="1234":
        print("Logged in successfully:)")
        while True:
            os.system('cls')
            print("1.Withdrawal")
            print("2.Balance check")
            print("3.Pin Change")
            print("4.Exit")
            b=int(input("Enter your choice : "))
            if(b==1):
                n=int(input("Enter the amount : "))
                if(n<bal) and (n%100)==0:
                    print("Take cash")
                    bal-=n
                    print("Your current amount balance is ",bal)
                    break;
            elif(b==2):
                print("Your current amount balance is ",bal)
                break;
            elif(b==3):
                c=int(input("Enter your old pin : "))
                d=int(input("Enter your new pin : "))
                e=int(input("confirm your new pin : "))
                if d!=e:
                    print("Invalid pin ")
                else:
                    print("Your pin is successfully changed:)")
                    
            elif b==4:
                break
    else:
        print("invalid password")
bal=20000
while True:
 print("---------->>>>>>>>WELCOME TO ATM<<<<<<<<----------")
 print("1.Admin\n2.User\n3.Exit")
 d=int(input("Enter your choice : "))
 if d==1:
    admin()
 elif d==2:
    user()
 else:
   break;
    
    
