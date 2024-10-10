
import csv
import pandas as pd

a='1'
b='1'
with open('C:\\Users\FILEPATH' , 'a') as app:
        print('Welcome to Admission Management System')
        print("Login to Continue")
        while True:
            Id=input('Enter your Id=')
            Ps=input('Enter Password=')
            if Id==a and Ps==b:
                break
            print('Invalid Credentials')
            print('Please re-enter your credentials')
        print('Welcome User')
        print('Enter 1 to Display current Data')
        ch=int(input('Enter your choice='))
        while True:
            if ch==1:
                break
            print('Invalid Input')
            print('Please Enter Correct input')
        print('*********Live Data**********')
        A=pd.read_csv('C:\\Users\FILEPATH')#df=pd.DataFrame(A)
        print(A)
        print('Editing Menu')
        print('Enter 2 To Delete Data')
        print('Enter 3 to Add Data')
        print('Enter 9 to Exit')
        cl=int(input('Enter your choice='))
        if cl==9:
            print('Thanks For Visiting')
        elif cl==3:
            n=int(input("Enter no. of records you want"))
            for i in range(n):
                L=[]
                Adm=int(input('Enter New Admission Number='))
                Fn=input('Enter Name of the Student=')
                DOB=input('Enter Date of Birth of the Student(as DD/MM/YYYY)=')
                S=input('Enter Gender of the Student(M/F)=')
                C = input('Enter Class of Student=')
                St=input('Enter Stream of Student(Main+Optional)')
                M=input('Enter Contact No. of Student=')
                N=input('Enter Aadhar No. of Student=')
                L.append(Adm)
                L.append(Fn)
                L.append(DOB)
                L.append(S)
                L.append(C)
                L.append(St)
                L.append(M)
                L.append(N)
                A.loc[len(A.index)]=L
                print(A)
                print('Enter 1 to save changes')
                s=int(input('Enter your choice='))
                if s==1:
                    writer_object=csv.writer(app)
                    writer_object.writerow(L)
            app.close()
            print("FILE SAVED SUCCESSFULLY")
            print('Enter 1 to View changes')
            I=int(input('Enter your choice='))
            if I==1:
                A1=pd.read_csv('C:\\Users\FILEPATH')
                print(A1)
        #app.close()        
        elif cl==2:
            app.close()
            L=[]
            app1=open('C:\\Users\FILEPATH', 'r' )
            Reader=csv.reader(app1)
            Admn_No=input('Enter Admn No. of the student to be deleted=')
            for row in Reader:
                print(row)
                if row[0]!=Admn_No:
                    L.append( row )
            app1.close()
            print(L)
            app2=open('C:\\Users\FILEPATH', 'w+', newline='')
            Writer=csv.writer(app2)
            Writer.writerows(L)
            #app2.seek(0)
            #Reader=csv.reader(app2)
            '''for row in Reader:
                print(row)'''
            app2.close()
            print('Data Deleted Successfully')
            D=int(input('Enter 1 to view Changes='))
            while True:
                if D==1:
                    break
                print('Invalid Input')
                print('Please Enter Correct input')
            A1= pd.read_csv('C:\\Users\FILEPATH')
            print(A1)
        else:
            print("worng input")
