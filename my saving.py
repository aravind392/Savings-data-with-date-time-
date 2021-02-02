#importing date and time

import datetime

#looping

i=1
loop=1
while i<=loop:

#heading

    print("\t""\t""Account Manage")  

#option 1

    print("\t""1.New Entry")

#option 2

    print("\t""2.To See Entered Entry")  

#option 3

    print("\t""3.Exit")

#geting option from user

    ch=int(input("\n""Enter A Option :"))   

#executing first option

    if ch==1:
    
    #defining function

        def new_entry() :
            now = datetime.datetime.now()
            acno= int(input("Enter A/C Number :"))
            prebal=int(input("Enter Previous Balance :"))
            add=int(input("Enter A Debit Value :"))
            sub=int(input("Enter A Credit Value :"))
            to=prebal+add
            tot=to-sub
            print("Your Entry Has Sucessfully Added")
        
       #creating text file and writing the the entered values in text file

            f = open('out.txt', 'a')
            f.write("\n""A/c Number: "'{}'.format(acno))
            f.write("\n""Previous Balance: "'{}'.format(prebal))
            f.write("\n""Debited: "'{}'.format(add))
            f.write("\n""Credited: "'{}'.format(sub))
            f.write("\n""Current Balance: "'{}'.format(tot))
            f.write("\n""Time: "'{}'.format(now))
            f.close
        
        #calling function

        new_entry()
    
    
#executing second option

    elif ch==2:
        print("\t""1.Serach By A/C No :")
        def check():
            op=int(input("Enter The Option :"))
            search=int(input("Enter Your A/c Number :"))

    #opening that text file 
    
            f =open('out.txt', 'r')
            input1 = f.readlines()
            f.close()

    #checking the search account number is in text file
    
            for search in input1:
                print (search)
        check()


#executing third option

    elif ch==3:
        exit()
    
#when other numbers are given this line of code will execute
    
    else:
        print("! Invalid Choice.")
