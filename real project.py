 # CLASS XII PROJECT                                         realproject
print ("""CREATED BY AASHISH TANWAR & ADITYA SHARMA """)

import pandas as pd
import mysql.connector as msc
from fpdf import FPDF
import webbrowser
import os
import platform
from datetime import date

        
mydb=msc.connect(host="localhost",
                 user="root",
                 passwd="mysql")
crs=mydb.cursor()
        
crs.execute("CREATE DATABASE IF NOT EXISTS sells")
mydb.commit()
crs.execute("USE sells")
        
qry1="CREATE TABLE IF NOT EXISTS Menu (Id varchar(20) Primary key,F_item varchar(20),Type varchar(20),Price varchar(20),Quantity varchar(20))"
crs.execute(qry1)
mydb.commit()

qry6="CREATE TABLE IF NOT EXISTS Cust_info (C_id varchar(20),C_name varchar(20),Contact_no varchar(20),Food_name varchar(20),Quantity varchar(20))"
crs.execute(qry6)
mydb.commit()

qry7="CREATE TABLE IF NOT EXISTS SALES(C_id varchar(20),C_name varchar(20),F_item varchar(20),Type varchar(20),Price varchar(20),Food_quantity varchar(20),F_id varchar(20))"
crs.execute(qry7)
mydb.commit()

qry00="CREATE TABLE IF NOT EXISTS Left_food (Id varchar(20) Primary key,F_item varchar(20),Type varchar(20),Price varchar(20),Quantity varchar(20))"
crs.execute(qry00)
mydb.commit()
        



'''qry2f1="INSERT INTO Menu VALUES('1','Mazza','Cold drink','35','10')"
qry2f2="INSERT INTO Menu VALUES('2','Samosa','Snacks','20','10')"
qry2f3="INSERT INTO Menu VALUES('3','Pastry','Pastry','60','10')"
crs.execute(qry2f1)
crs.execute(qry2f2)
crs.execute(qry2f3)
mydb.commit()

qry3b1="INSERT INTO Left_food VALUES('1','Mazza','Cold drink','35','10')"
qry3b2="INSERT INTO Left_food VALUES('2','samosa','snacks','20','10')"
qry3b3="INSERT INTO Left_food VALUES('3','pastry','pastry','60','10')"
crs.execute(qry3b1)
crs.execute(qry3b2)
crs.execute(qry3b3)
mydb.commit()'''

        



'''qry2="INSERT INTO Menu VALUES((),(),(),())"
crs.execute(qry2)'''


crs.close()




while True:
    apa=str(input("Enter the password to use the software:"))
    if apa=="apa":
        try:
            #ADDITION
            def insert():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    print("INSERT NEW DATA")
                    qwerty1="SELECT * FROM Menu"
                    crs.execute(qwerty1)
                    QWERTY1=crs.fetchall()
                    dfgh=pd.DataFrame(QWERTY1,columns=['ID','Food item','Type','Price','Quantity'])
                    print(dfgh)
                    print()
                    Id=str(input("Enter new ID(only integers)="))
                    F_item=str(input("Enter food item="))
                    Type=str(input("Enter type of "+str(F_item)+"="))
                    Price=str(input("Enter price of "+str(F_item)+"="))
                    quantity=str(input("Enter the quantity of "+str(F_item)+"="))
                    
                    qry31="INSERT INTO Menu VALUES (%s,%s,%s,%s,%s)"
                    data31=(Id,F_item,Type,Price,quantity)
                    crs.execute(qry31,data31)
                    mydb.commit()

                    qry3f1="INSERT INTO Left_food VALUES (%s,%s,%s,%s,%s)"
                    data3f1=(Id,F_item,Type,Price,quantity)
                    crs.execute(qry3f1,data3f1)
                    mydb.commit()
                    
                    print(crs.rowcount,"RECORDS INSERTED")
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to insert record")

            #DELETE
            def delete():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    print("****Delete from data****")
                    
                    qry41="SELECT * FROM Menu"
                    crs.execute(qry41)
                    data41=crs.fetchall()
                    df41=pd.DataFrame(data41,columns=['Id','F_item','Type','Price','Quantity'])
                    print(df41)
                    print()
                    f_idel=str(input("Enter the number of food Id to be deleted = "))               
                    quantity=str(input("Enter the left quantity = "))
                    
                    if quantity=='0':
                        qry4fof2="DELETE FROM Menu WHERE Id = %s"
                        crs.execute(qry4fof2,(f_idel,))
                        mydb.commit()

                        qry4ofo2="DELETE FROM Left_food WHERE Id = %s"
                        crs.execute(qry4ofo2,(f_idel,))
                        mydb.commit()
                        
                    else:
                        qry42="UPDATE Menu SET Quantity=%s WHERE Id = %s"
                        data42=(quantity,f_idel)
                        crs.execute(qry42,data42)
                        mydb.commit()

                        qry4f2="UPDATE Left_food SET Quantity = %s WHERE Id = %s"
                        data4f2=(quantity,f_idel)
                        crs.execute(qry4f2,data4f2)
                        mydb.commit()
                    
                    print(crs.rowcount,"Record wanted deleted")
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to delete the menu information")

            #MODIFY
            def update():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    print("****Modification in Menu records****")
                    qry5="SELECT * FROM Menu"
                    crs.execute(qry5)
                    data5=crs.fetchall()
                    df5=pd.DataFrame(data5,columns=['Id','F_item','Type','Price','Quantity'])
                    print(df5)
                    print()
                    Id=str(input("Enter the number of ID you want to update:"))
                    F_item=str(input("Enter the new name of food_item:"))
                    Type=str(input("Enter the new type of "+str(F_item)+":"))
                    Price=str(input("Enter the new price of per "+str(F_item)+":"))
                    quantity=str(input("Enter thye new quantity of "+str(F_item)+"="))
                    
                    qry51="UPDATE Menu SET F_item=%s,Type=%s,Price=%s,Quantity=%s WHERE Id=%s"
                    data51=(F_item,Type,Price,quantity,Id)
                    crs.execute(qry51,data51)
                    mydb.commit()

                    qry5f1="UPDATE Left_food SET F_item=%s,Type=%s,Price=%s,Quantity=%s WHERE Id=%s"
                    data5f1=(F_item,Type,Price,quantity,Id)
                    crs.execute(qry5f1,data5f1)
                    mydb.commit()
                    
                    print(crs.rowcount,"Record has been updated")
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to update the Menu information")




            #SELLING PROCESS
            def sell():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    print("@*@*@*@*@SELLING ITEMS@*@*@*@*@")
                    qry8="SELECT * FROM Left_food"
                    crs.execute(qry8)
                    data8=crs.fetchall()
                    df8=pd.DataFrame(data8,columns=['Id','F_item','Type','Price','Quantity'])
                    print(df8)
                    print()
                    C_id=str(input("Enter the code of customer = "))
                    C_name=str(input("Enter the name of customer = "))
                    C_contact=str(input("Enter the contact number of customer = "))
                    print()
                    k=1
                    while k!=0:
                        Id=str(input("Enter food ID =  "))
                        quantity=str(input("Enter the quantity of food item required = "))
                        print()
                        inpt=str(input("Enter any alphabet to not buy more products or if then enter any key except alphabet = "))
                        if inpt.isalpha():
                            qry8f1="SELECT * FROM Left_Food WHERE ID = %s"
                            crs.execute(qry8f1,(Id,))
                            data8f1=crs.fetchall()
                          
                            B=[]
                            for i in data8f1:
                                B.append(i)
                            print(B)
                                
                            
                            qry81="INSERT INTO Cust_info VALUES(%s,%s,%s,%s,%s)"
                            data81=(C_id,C_name,C_contact,B[0][1],quantity)
                            crs.execute(qry81,data81)
                            mydb.commit()
                            print()
                            totalcosts=str(float(B[0][3])*float(quantity))
                            

                            qry82="INSERT INTO SALES VALUES(%s,%s,%s,%s,%s,%s,%s)"
                            data82=(C_id,C_name,B[0][1],B[0][2],B[0][3],quantity,B[0][0])
                            crs.execute(qry82,data82)
                            mydb.commit()
                            print()

                            lftqty=str(int(B[0][4])-int(quantity))
                            qry8f2="UPDATE Left_food SET Quantity=%s WHERE ID = %s"
                            data8f2=(lftqty,Id)
                            crs.execute(qry8f2,data8f2)
                            mydb.commit()
                            
                            qry8f2="UPDATE Menu SET Quantity=%s WHERE ID = %s"
                            data8f2=(lftqty,Id)
                            crs.execute(qry8f2,data8f2)
                            mydb.commit()
                            print()
                            k=0
                        else:
                            print("JESUS")
                            qry8f1="SELECT * FROM Left_Food WHERE ID = %s"
                            crs.execute(qry8f1,(Id,))
                            data8f1=crs.fetchall()
                            

                            B=[]
                            for i in data8f1:
                                B.append(i)
                            print(B)
                                
                            # kjgedrklyjteroyjtreyoijert;yoijersryekjrhlwituphe4rt9u85tjrgkjmmhlfghmgfselr;yjktseo;rit
                            
                            qry81="INSERT INTO Cust_info VALUES(%s,%s,%s,%s,%s)"
                            data81=(C_id,C_name,C_contact,B[0][1],quantity)
                            crs.execute(qry81,data81)
                            mydb.commit()
                            print()
                            
                            

                            qry82="INSERT INTO SALES VALUES(%s,%s,%s,%s,%s,%s,%s)"
                            data82=(C_id,C_name,B[0][1],B[0][2],B[0][3],quantity,B[0][0])
                            crs.execute(qry82,data82)
                            mydb.commit()
                            print()

                            lftqty=str(int(B[0][4])-int(quantity))
                            qry8f2="UPDATE Left_food SET Quantity=%s WHERE ID = %s"
                            data8f2=(lftqty,Id)
                            crs.execute(qry8f2,data8f2)
                            mydb.commit()
                            print()

                            qry8f2="UPDATE Menu SET Quantity=%s WHERE ID = %s"
                            data8f2=(lftqty,Id)
                            crs.execute(qry8f2,data8f2)
                            mydb.commit()
                            print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to purchase, please try again")

            #Generate pdf        
            def generate_bill():
                try:
                    mydb=msc.connect(host='localhost',
                                     user='root',
                                     passwd='mysql',
                                     database='sells')
                    crs=mydb.cursor()
                    print("Welcome for generating cash memo")
                    print()
                    today = date.today()
                    C_name=str(input("Enter the name of customer whose bill have to be generated:"))
                    qry9f="SELECT * FROM Sales WHERE C_name = %s"
                    crs.execute(qry9f,(C_name,))
                    myresult=crs.fetchall()
                    print(myresult)
                    qryft1="SELECT * FROM Cust_info WHERE C_name = %s"
                    crs.execute(qryft1,(C_name,))
                    dataft1=crs.fetchall()
                    cost=0

                        
                    A=[]
                       
                    #Generate pdf for billing
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",size=18)
                    pdf.cell(0,5,'Food Bill',ln=1, align="C")
                    pdf.set_font("Arial",size=22)
                    pdf.cell(0,5,'AA Bakers','B',ln=1, align="C")
                    pdf.set_font("Arial",size=10)
                    pdf.cell(0,5,'C-Scheme, Jaipur',ln=1, align="C")
                    pdf.set_font("Arial",size=14)
                    pdf.cell(0,5,'Name: '+str(C_name),ln=1, align="L")
                    pdf.cell(0,5,'Date: '+str(today),ln=1,align="R")
                    pdf.cell(0,5,'Contact no: '+str(dataft1[0][2]), ln=1, align="L")
                    pdf.set_font("Arial",size=12)
                    pdf.cell(0,0,"____________________________________________________________________________________________________________",ln=1,align='L')
                    pdf.cell(16,10,"Food_ID           NAME_OF_FOOD_ITEM             COST_PER_PRODUCT         QUANTITY",ln=1,align="L")
                    pdf.cell(0,0,"_____________________________________________________________________________________________________________",0,1,align='L')
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    for i in myresult:
                        A.append(i)
                        pdf.cell(17,5,str(i[6]),0,0,align="C")
                        pdf.cell(75,5,str(i[2]),0,0,align="C")
                        pdf.cell(50,5,str(i[4]),0,0,align="C")
                        pdf.cell(30,5,str(i[5]),0,1,align="C")
                        cost+=float(float(i[4])*float(i[5]))
                    pdf.cell(0,0,"____________________________________________________________________________________________________________",ln=1,align='L')    

                    gst=float(0.18*cost)
                    tcost=float(gst+cost)
                    pdf.cell(0,10,"Total cost: "+str(cost),ln=1,align="R")
                    pdf.cell(0,10,"GST amount:"+str(gst),ln=1,align="R")
                    pdf.cell(0,10,"Grand Total:"+str(tcost),ln=1,align="R")
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    pdf.cell(0,10,"   ",ln=1,align="R")
                    pdf.cell(0,10,"signature",ln=1,align="R")

                    fnm=str(C_name)+".pdf"
                    print(fnm)
                    pdf.output(fnm)
                    webbrowser.open(fnm)
                    pdf=FPDF(orientation='P', unit='mm', format='A4')
                    print(A)    
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to generate bill, please try again")



            #DISPLAY
            def display_M():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    qry9="SELECT * FROM Menu"
                    print()
                    crs.execute(qry9)
                    data9=crs.fetchall()
                    df9=pd.DataFrame(data9,columns=['Id','F_item','Type','Price','Quantity'])
                    print(df9)
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to DISPLAY table")


            def display_C():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    qry91="SELECT * FROM Cust_info"
                    crs.execute(qry91)
                    data91=crs.fetchall()
                    df91=pd.DataFrame(data91,columns=['C_id','C_name','C_contact','Food_name','Quantity'])
                    print(df91)
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to display the data of customers")

                    
            def display_sp():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    qry92="SELECT * FROM SALES"
                    crs.execute(qry92)
                    data92=crs.fetchall()
                    df92=pd.DataFrame(data92,columns=['ID','Customer name','Food item','Type','Price','Food Quantity'])
                    print(df92)
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to display the information of sales")
                    

            def display_lftfd():
                try:
                    mydb=msc.connect(host="localhost",
                                     user="root",
                                     passwd="mysql",
                                     database="sells")
                    crs=mydb.cursor()
                    qry9f2="SELECT * FROM Left_food"
                    crs.execute(qry9f2)
                    data9f2=crs.fetchall()
                    df9f2=pd.DataFrame(data9f2,columns=['ID','F_item','Type','Price','Quantity'])
                    print(df9f2)
                    print()
                    print()
                    crs.close()
                except mysql.connector.Error as error:
                    print("Unable to display the information of sales")

                    

            #PROGRAM
            k=0
            while (k!=5):
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("@@@@@@@WELCOME TO AASHISH & ADITYA mysql@@@@@@@")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print("1. MENU MANAGEMENT")
                print("2. SALES")
                print("3. SALES REPORT")
                print("4. CUSTOMER REPORT")
                print("5. QUIT")
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                c1=str(input("Enter your choice:"))
                if c1=="1":
                    print("@@@@@@@@@@@@@@@@@@@@@@@")
                    print("@@@@MENU MANAGEMENT@@@@")
                    print("@@@@@@@@@@@@@@@@@@@@@@@")
                    print("1 INSERTING OF NEW DATA ")
                    print("2 DELETION  OF DATA")
                    print("3 MODIFICATION OF DATA")
                    print("4 BACK")
                    print("@@@@@@@@@@@@@@@@@@@@@@@")
                    c11=str(input("Enter your choice:"))
                    if c11=="1":
                        insert()
                    elif c11=="2":
                        delete()
                    elif c11=="3":
                        update()
                    elif c11=="4":
                        print()
                        print()
                        continue
                elif c1=="2":
                    print("@@@@@@@@@@@@@@@@")
                    print("@@@@@SALES@@@@@@")
                    print("@@@@@@@@@@@@@@@@")
                    print("1 START SELL")
                    print("2 Generate Bill")
                    print("3 BACK")
                    print("@@@@@@@@@@@@@@@@")
                    c12=str(input("Enter your choice:"))
                    if c12=="1":
                        sell()
                    elif c12=="2":
                        generate_bill()
                    elif c12=="3":
                      print()
                      print()
                      continue
                elif c1=="3":
                    print("@@@@@@@@@@@@@@@@")
                    print("@@SALES REPORT@@")
                    print("@@@@@@@@@@@@@@@@")
                    print("1 DISPLAY MENU RECORDS ")
                    print("2 DISPLAY SELLING PROCESS")
                    print("3 DISPLAY LEFT FOODS")
                    print("4 BACK")
                    print("@@@@@@@@@@@@@@@@")
                    c13=str(input("Enter your choice:"))
                    if c13=="1":
                        print("\tMENU RECORDS")
                        display_M()
                    elif c13=="2":
                        print("\t SELLING PROCESS")
                        display_sp()
                    elif c13=="3":
                        print("\t LEFT FOODS")
                        display_lftfd()
                    elif c13=="4":
                        print()
                        print()
                        continue
                elif c1=="4":
                    print("@@@@ CUSTOMER REPORT @@@@")
                    display_C()
                elif c1=="5":
                    print("@@@@@@@@ THANKS FOR VISITING @@@@@@@@")
                    k=5
                    print('$'*60)
                    print('$'*60)
                    print('$'*60)
                    print('$'*60)
                    print('$'*60)
                    break
        except:
            pass
    else:
        print("You have inserted wrong password")
        print()
        poiu=str(input("Enter any alphabet to exit and to apply again please enter any key except alphabet:"))
        if poiu.isalpha():
            print("Thanks for using our service.")
            acv=str(input("Enter any key to exit:"))
            break
        else:
            continue





    



