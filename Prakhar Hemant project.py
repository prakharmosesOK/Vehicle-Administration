# Class XII Science Project
print("""MADE BY -  1. PRAKHAR MOSES
                    2. HEMANT BHERWAL
                    3. ANSHUL           """)



'''------------------------------------------------------------------------------
-------------------------------Checking password---------------------------------
------------------------------------------------------------------------------'''

while True:
    a1=str(input("Enter the password of Tours and Travel Agency:"))
    if a1=="12345":
        

        try:
            import pandas as pd
            import mysql.connector as msc
            from fpdf import FPDF
            import webbrowser
            import os
            import platform
            from datetime import date

           
            
            mydb=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
            crs=mydb.cursor()

            qry1="CREATE TABLE IF NOT EXISTS Tours (Vehicle_no varchar(20),Vehicle_name varchar(20),Type varchar(20),Rate_per_km varchar(10),Medium varchar(5),Going_to varchar(20),Distance varchar(20))"
            crs.execute(qry1)
            

            '''qry21="INSERT INTO Tours VALUES(1001,'Honda city','Car','42','Road','Ajmer','135')"
            qry22="INSERT INTO Tours VALUES(1002,'Swift Dzire','Car','25','Road','Bikaner','335')"
            qry23="INSERT INTO Tours VALUES(1003,'Wrangler','Jeep','37','Road','Alwar','160')"
            qry24="INSERT INTO Tours VALUES(1004,'Jeep Compass','Jeep','40','Road','Delhi','273')"
            qry25="INSERT INTO Tours VALUES(1005,'Trax','Car','30','Road','Amer','14')"
            qry26="INSERT INTO Tours VALUES(1006,'Tahoe Suburban','Car','35','Road','Mumbai','1146')"
            qry27="INSERT INTO Tours VALUES(1007,'Innova','Car','18','Road','Jodhpur','358')"
            qry28="INSERT INTO Tours VALUES(1008,'i 20','Car','14','Road','Pushkar','142')"
            qry29="INSERT INTO Tours VALUES(1009,'WagonR','Car','13','Road','Chittorgarh','300')"
            qry211="INSERT INTO Tours VALUES(1010,'MG Hector','Car','30','Road','Sikar','180')"
            crs.execute(qry21)
            crs.execute(qry22)
            crs.execute(qry23)
            crs.execute(qry24)
            crs.execute(qry25)
            crs.execute(qry26)
            crs.execute(qry27)
            crs.execute(qry28)
            crs.execute(qry29)
            crs.execute(qry211)
            mydb.commit()'''



            qry6o2="CREATE TABLE IF NOT EXISTS Vehicle_unhired (Vehicle_no varchar(20),Vehicle_name varchar(20),Type varchar(20),Rate_per_km varchar(5),Medium varchar(5),Going_to varchar(20),Distance varchar(20))"
            crs.execute(qry6o2)

            '''qry6o21="INSERT INTO Vehicle_unhired VALUES(1001,'Honda city','Car','42','Road','Ajmer','135')"
            qry6o22="INSERT INTO Vehicle_unhired VALUES(1002,'Swift Dzire','Car','25','Road','Bikaner','335')"
            qry6o23="INSERT INTO Vehicle_unhired VALUES(1003,'Wrangler','Jeep','37','Road','Alwar','160')"
            qry6o24="INSERT INTO Vehicle_unhired VALUES(1004,'Jeep Compass','Jeep','40','Road','Delhi','273')"
            qry6o25="INSERT INTO Vehicle_unhired VALUES(1005,'Trax','Car','30','Road','Amer','14')"
            qry6o26="INSERT INTO Vehicle_unhired VALUES(1006,'Tahoe Suburban','Car','35','Road','Mumbai','1146')"
            qry6o27="INSERT INTO Vehicle_unhired VALUES(1007,'Innova','Car','18','Road','Jodhpur','358')"
            qry6o28="INSERT INTO Vehicle_unhired VALUES(1008,'i 20','Car','14','Road','Pushkar','142')"
            qry6o29="INSERT INTO Vehicle_unhired VALUES(1009,'WagonR','Car','13','Road','Chittorgarh','300')"
            qry6o211="INSERT INTO Vehicle_unhired VALUES(1010,'MG Hector','Car','30','Road','Sikar','180')"
            crs.execute(qry6o21)
            crs.execute(qry6o22)
            crs.execute(qry6o23)
            crs.execute(qry6o24)
            crs.execute(qry6o25)
            crs.execute(qry6o26)
            crs.execute(qry6o27)
            crs.execute(qry6o28)
            crs.execute(qry6o29)
            crs.execute(qry6o211)
            mydb.commit()'''



            qry6o1="CREATE TABLE IF NOT EXISTS Cust_info (Customer_code varchar(10),Name varchar(20),Contact_no varchar(12),Going_to varchar(20),No_of_days varchar(3),Vehicle_number_hired varchar(20),Vehicle_name varchar(20))"
            crs.execute(qry6o1)





            qry6o2="CREATE TABLE IF NOT EXISTS Vehicle_hired (Vehicle_no varchar(20),Vehicle_name varchar(20),Type varchar(20),Rate_per_km varchar(5),Medium varchar(5),Going_to varchar(20),Distance varchar(20))"
            crs.execute(qry6o2)
            

            
            crs.close()

            '''------------------------------------------------------------------------------
            --------------------------------Insert Command-----------------------------------
            ------------------------------------------------------------------------------'''
            
            def insert():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    print("****Addition of new vehicle****")
                    qry123="SELECT * FROM Tours"
                    curs.execute(qry123)
                    data123=curs.fetchall()
                    df123=pd.DataFrame(data123,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df123)
                    vno=str(input("Enter new vehicle number:"))
                    vname=str(input("Enter vechile name:"))
                    vtype=str(input("Enter vechile type:"))
                    vrate=str(input("Enter rate per km of vehicle (in numbers):"))
                    vmedium=str(input("Enter the medium of travelling of vehicle:"))
                    varrival=str(input("Enter the place where the vehicle will go:"))
                    vkm=str(input("Enter the distance of "+str(varrival)+" from Jaipur:"))
                    
                    qry3o1="INSERT INTO Tours VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    data3o1=(vno,vname,vtype,vrate,vmedium,varrival,vkm)
                    curs.execute(qry3o1,data3o1)
                    mydbs.commit()
                    

                    qry3o1="INSERT INTO Vehicle_unhired VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    data3o1=(vno,vname,vtype,vrate,vmedium,varrival,vkm)
                    curs.execute(qry3o1,data3o1)
                    mydbs.commit()
                    
                    
                    print(curs.rowcount,"Vehicle inserted")
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to insert new vehicle data")

            '''------------------------------------------------------------------------------
            ----------------------------------Delete Command---------------------------------
            ------------------------------------------------------------------------------'''
            def delete():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    print("****Deletion of vehicle****")
                    qry4o1="SELECT * FROM Tours"
                    curs.execute(qry4o1)
                    data4o1=curs.fetchall()
                    df4o1=pd.DataFrame(data4o1,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df4o1)
                    print()
                    vnumdel=str(input("Enter the number of vehicle to be deleted:"))
                
                    qry4o2="DELETE FROM Tours WHERE Vehicle_no LIKE %s"
                    curs.execute(qry4o2,(vnumdel,))
                    mydbs.commit()

                    qry4o2="DELETE FROM Vehicle_unhired WHERE Vehicle_no LIKE %s"
                    curs.execute(qry4o2,(vnumdel,))
                    mydbs.commit()
                    
                    print(curs.rowcount,"Vehicle record have been deleted")
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to delete the vehicle information")

            '''------------------------------------------------------------------------------
            ----------------------------------Modify Command---------------------------------
            ------------------------------------------------------------------------------'''
            def update():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    print("****Modification in vehicle records****")
                    qry5o1="SELECT * FROM Tours"
                    curs.execute(qry5o1)
                    data5o1=curs.fetchall()
                    df5o1=pd.DataFrame(data5o1,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df5o1)
                    vnumber=str(input("Enter the number of vehicle whose data you want to update:"))
                    vname=str(input("Enter the new name of vehicle:"))
                    vtype=str(input("Enter the new type of vehicle:"))
                    vrate=str(input("Enter the new rate of vehicle per km:"))
                    vmedium=str(input("Enter the new medium of travelling of vehicle:"))
                    varrival=str(input("Enter the new arrival place of vehicle:"))
                    vkm=str(input("Enter the distance of "+str(varrival)+" from Jaipur:"))
                    
                    qry5o2="UPDATE Tours SET Vehicle_name=%s,Type=%s,Rate_per_km=%s,Medium=%s,Going_to=%s,Distance=%s WHERE Vehicle_no=%s"
                    data5o2=(vname,vtype,vrate,vmedium,varrival,vkm,vnumber)
                    curs.execute(qry5o2,data5o2)
                    mydbs.commit()

                    qry5o3="UPDATE Vehicle_unhired SET Vehicle_name=%s,Type=%s,Rate_per_km=%s,Medium=%s,Going_to=%s,Distance=%s WHERE Vehicle_no=%s"
                    data5o3=(vname,vtype,vrate,vmedium,varrival,vkm,vnumber)
                    curs.execute(qry5o3,data5o3)
                    mydbs.commit()

                    """qry5o2="UPDATE Vehicle_hired SET Vehicle_name=%s,Type=%s,Rate_per_km=%s,Medium=%s,Arrival_place=%s,Distance=%s WHERE vnumber=%s"
                    data5o2=(vname,vtype,vrate,vmedium,varrival,vkm,vnumber)
                    curs.execute(qry5o2,data5o2)
                    mydbs.commit()"""
                    
                    print(curs.rowcount,"Vehicle record has been updated")
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to update the vehicle information")


                    
                '''------------------------------------------------------------------------------
                ----------------------------------Code for Hiring of Vehicle---------------------
                ------------------------------------------------------------------------------'''
          
            def hire_vehicle():
                try:
                    mydbs=msc.connect(host="localhost",
                                      user="root",
                                      passwd="mysql",
                                      database="mysql")
                    curs=mydbs.cursor()
                    print("****Hiring of vehicle****")
                    qry7o1="SELECT * FROM Vehicle_unhired"
                    curs.execute(qry7o1)
                    data7o1=curs.fetchall()
                    df7o1=pd.DataFrame(data7o1,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df7o1)

                    
                    cust_code=str(input("Enter the code of customer = "))
                    cust_name=str(input("Enter the name of customer = "))
                    cust_contact=str(input("Enter the contact number of customer = "))
                    going_to=str(input("Enter the place you want to go = "))
                    No_of_days=str(input("Enter the no of days of hiring = "))
                    vcode_hired=str(input("Enter the no of vehicle hired = "))

                    qry7o1o1="SELECT * FROM Vehicle_unhired WHERE Vehicle_no = %s"
                    curs.execute(qry7o1o1,(vcode_hired,))
                    data7o1o1=curs.fetchall()

                    A=[]
                    for i in data7o1o1:
                        A.append(i)
                    
                    
                    
                    qry7o2="INSERT INTO Cust_info VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    data7o2=(cust_code,cust_name,cust_contact,going_to,No_of_days,vcode_hired,A[0][1])
                    curs.execute(qry7o2,data7o2)
                    mydbs.commit()

                    qry7o3="INSERT INTO Vehicle_hired VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    data7o3=(vcode_hired,A[0][1],A[0][2],A[0][3],A[0][4],A[0][5],A[0][6])
                    curs.execute(qry7o3,data7o3)
                    mydbs.commit()
                    print()

                    qry147="DELETE FROM Vehicle_unhired WHERE Vehicle_no = %s"
                    curs.execute(qry147,(vcode_hired,))
                    mydbs.commit()
                    print()
                    


                    qry156="CREATE TABLE IF NOT EXISTS Bill (Customer_name varchar(20),Going_from varchar(20),Going_to varchar(20),No_of_days varchar(20),Name_of_hired_vehicle varchar(20),Rate_per_km varchar(20),Total_Cost varchar(20))"
                    curs.execute(qry156)
                    
                    
                    city="Jaipur"
                    costs=str(float(A[0][3])*float(A[0][6]))
                    qry157="INSERT INTO Bill VALUES(%s,%s,%s,%s,%s,%s,%s)"
                    data157=(cust_name,city,going_to,No_of_days,A[0][1],A[0][3],costs)
                    curs.execute(qry157,data157)
                    mydbs.commit()
                    gst=float(costs)*(0.18)
                    totalcost=gst+float(costs)
                    today = date.today()
           
                    

                    qry157o1="select * from Bill WHERE Customer_name = %s"
                    curs.execute(qry157o1,(cust_name,))
                    myresult=curs.fetchall()

                    L=[]

                    '''------------------------------------------------------------------------------
                    ----------------------------------Generate Pdf-----------------------------------
                    ------------------------------------------------------------------------------'''
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.cell(0,5,"CASH INVOICE", ln=1, align="C")
                    pdf.set_font("Arial",'B',size=22)
                    pdf.cell(0,5,'PHA Tours and Travels', ln=1, align="C")
                    pdf.set_font("Arial", size=10)
                    pdf.cell(0,5,'72/32, Patel Marg, Jaipur, Rajasthan', ln=1, align="C")
                    pdf.cell(0,5,'Phone : 985642139', ln=1, align="C")
                    pdf.set_font("Arial", size=14)
                    pdf.cell(0,5,'Date:'+str(today),ln=1,align="R")
                    pdf.cell(0,5,'Name of Customer :'+str(cust_name), ln=1, align="L")
                    pdf.cell(0,5,'Phone Number :'+str(cust_contact), ln=1, align="L")
                    pdf.set_font("Arial", size=12)
                    pdf.cell(0,0,"---------------------------------------------------------------------------------------------------------------------------------------",ln=1,align="L")
                    pdf.cell(160,10,"  From       To         Number_of_days    Name_of_hired_vehicle    Rate_per_km           Total_Cost",ln=1,align="L")
                    pdf.cell(0,0,"---------------------------------------------------------------------------------------------------------------------------------------",0,1,align="L")
                    for i in myresult:
                        L.append(i)
                        print(i)
                        pdf.cell(18,5,str(i[1]),0,0, align="C")
                        pdf.cell(20,5,str(i[2]),0,0, align="C")
                        pdf.cell(25,5,str(i[3]),0,0, align="C")
                        pdf.cell(38,5,str(i[4]),0,0, align="C")
                        pdf.cell(46,5,str(i[5]),0,0, align="C") 
                        pdf.cell(45,5,str(i[6]),0,1, align="C")
                    pdf.cell(0,0,"--------------------------------------------------------------------------------------------------------------------------------------",ln=1,align="L")

                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"GST amount "+str(gst),ln=1,align="R")
                    pdf.cell(0,10,"Grand total amount "+str(totalcost),align="R")
                    pdf.cell(0,10,"      ",ln=1,align="C")
                    pdf.cell(0,10,"Signature ",ln=1,align="R")

                    fnm=cust_name+".pdf"
                    print(fnm)
                    pdf.output(fnm)
                    pdf=FPDF(orientation='P', unit='mm', format='A4')

                    
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to book vehicle for you, please try again")



                '''------------------------------------------------------------------------------
                ----------------------------------Display Command--------------------------------
                ------------------------------------------------------------------------------'''

                '''------------------------------------------------------------------------------
                ----------------------------------Displaying Tours-------------------------------
                ------------------------------------------------------------------------------'''

            def display_T():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    qry8o1="SELECT * FROM Tours"
                    curs.execute(qry8o1)
                    data8o1=curs.fetchall()
                    df8o1=pd.DataFrame(data8o1,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df8o1)
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to display table")
                    
                '''------------------------------------------------------------------------------
                -----------------------------Displaying Customor Report--------------------------
                ------------------------------------------------------------------------------'''

            def display_C():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    qry8o2="SELECT * FROM Cust_info"
                    curs.execute(qry8o2)
                    data8o2=curs.fetchall()
                    df8o2=pd.DataFrame(data8o2,columns=['Customer_code','Name','Contact_no','Going_to','No_of_days','Vehicle_number_hired','Vehicle_name'])
                    print(df8o2)
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to display the data of customers.")
                    
                '''------------------------------------------------------------------------------
                ------------------------------Displaying Vehicle Hired---------------------------
                ------------------------------------------------------------------------------'''

            def display_Vh():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    qry8o3="SELECT * FROM Vehicle_hired"
                    curs.execute(qry8o3)
                    data8o3=curs.fetchall()
                    df8o3=pd.DataFrame(data8o3,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df8o3)
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to display the information about hired vehicle")
                    
                '''------------------------------------------------------------------------------
                ----------------------------Displaying Vehicle Unhired---------------------------
                ------------------------------------------------------------------------------'''

            def display_Vuh():
                try:
                    mydbs=msc.connect(host="localhost",
                             user="root",
                             passwd="mysql",
                             database="mysql")
                    curs=mydbs.cursor()
                    qry8o4="SELECT * FROM Vehicle_unhired"
                    curs.execute(qry8o4)
                    data8o4=curs.fetchall()
                    df8o4=pd.DataFrame(data8o4,columns=['Vehicle_no','Vehicle_name','Type','Rate_per_km','Medium','Arrival_place','Distance'])
                    print(df8o4)
                    print()
                    print()
                    curs.close()
                except mysql.connector.Error as error:
                    print("Failed to display the information about unhired vehicle")





            '''------------------------------------------------------------------------------
            ----------------------------------Program code-----------------------------------
            ------------------------------------------------------------------------------'''
            k=0
            while (k!=5):
                print("************************************************")
                print("**********Welcome to Tours and Travels**********")
                print("************************************************")
                print("1 Vehicle Management")
                print("2 Hiring Vehicle")
                print("3 Vehicle report")
                print("4 Customer report")
                print("5 Quit the system")
                print("************************************************")
                choice1=str(input("Enter your choice:"))
                if choice1=="1":
                    print("**************************")
                    print("****Vehicle Management****")
                    print("**************************")
                    print("1 Addition of  new vehicle")
                    print("2 Deletion of vehicle")
                    print("3 Modification of vehicle record")
                    print("4 Back")
                    print("**************************")
                    choice1o1=str(input("Enter your choice:"))
                    if choice1o1=="1":
                        insert()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                    elif choice1o1=="2":
                        delete()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                    elif choice1o1=="3":
                        update()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                    elif choice1o1=="4":
                        print()
                        print()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        continue
                elif choice1=="2":
                    print("**********************")
                    print("****Hiring Vehicle****")
                    print("**********************")
                    print("1 Start hiring vehicle")
                    print("2 Back")
                    print("**********************")
                    choice1o2=str(input("Enter your choice:"))
                    if choice1o2=="1":
                        hire_vehicle()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                    elif choice1o2=="2":
                        print()
                        print()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        continue
                elif choice1=="3":
                    print("**********************")
                    print("****Vehicle report****")
                    print("**********************")
                    print("1 Display total vehicle records")
                    print("2 Display hired vehicle records")
                    print("3 Display unhired vehicle record:")
                    print("4 Back")
                    print("**********************")
                    choice1o3=str(input("Enter your choice:"))
                    if choice1o3=="1":
                        print("\tTotal vehicle records")
                        display_T()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        print()
                        print()
                    elif choice1o3=="2":
                        print("\tHired vehicles")
                        display_Vh()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        print()
                        print()
                    elif choice1o3=="3":
                        print("\tUnhired vehicles")
                        display_Vuh()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        print()
                        print()
                    elif choice1o3=="4":
                        print()
                        print()
                        a=input("Enter any key to proceed:")
                        print(os.system('cls'))
                        continue
                elif choice1=="4":
                    print("****Customer reports****")
                    display_C()
                    a=input("Enter any key to proceed:")
                    print(os.system('cls'))
                    print()
                elif choice1=="5":
                    print("****Thanks for using our service****")
                    k=5
                    print('-'*60)
                    print('-'*60)
                    print('-'*60)
                    print('-'*60)
                    print('-'*60)
                    apple=input("Enter any key to exit:")
                    print(os.system('cls'))
        except:
            pass
    else:
            print("Password is incorrect,\nPlease enter the correct password.")
            a2=str(input("Enter any number to again apply for password or press any alphabet to exit:"))
            print()
            if a2.isalpha():
                print("Thanks for using our service.")
                break

