from datetime import date
import random
import string
import mysql.connector
my_db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Alliance@123', database = 'Bank', buffered = True)

def admin():
    account_ID = input("Account ID: ")
    password = input("Enter Password: ")
    
    if account_ID == "admin" and password == "secret":
        return True
    else:
        return False

def New_Account():
    branch = input("Branch Name: ")
    name = input("Name: ")
    age = int(input("Age: "))
    dob = input("Date of Birth: ")
    address = input("Address: ")
    contact = input("Phone Number: ")
    type = input("Account Type: ")
    
    if True:
        key = str(random.randint(100000,1000000))
        print("Unique Account Number: ",end=' ')
        print(key)
    
    acc_no = input("Account Number: ")
    data_1 = (branch, name, age, dob, address, contact, type, acc_no)
    sql_1 = ('insert into account values(%s,%s,%s,%s,%s,%s,%s,%s)')
    x = my_db.cursor()
    x.execute(sql_1, data_1)
    my_db.commit()
    print("...Data entered successfully...")
    main()

def Deposit():
    acc_no = input("Enter Account Number: ")
    description = input("Transaction type: ")
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    key = str(ran)
    amt = int(input("Enter Deposit Amount: "))
    dt = date.today()
    bal = 0
    data_2 = (dt, description, key, amt, bal, acc_no)
    sql_2 = ('insert into transaction(Date_time,Description,Reference,Amount,Balance,Account_Number) values(%s,%s,%s,%s,%s,%s)')
#    q = (acc_no)
#    a = ("select Balance from transaction where Account_Number=%s" % (acc_no))
    x = my_db.cursor()
    x.execute(sql_2,data_2)
#    my_db.commit()
    x.execute("select Balance from transaction where Account_Number=%s" % (acc_no))
    result = x.fetchone()
    r = result[0] + amt
#   print(r)
#    sql_3 = ("update transaction set Balance=%s where Account_Number=%s" % (r,acc_no))
#    d = (r,acc_no)
    x.execute("update transaction set Balance=%s where Account_Number=%s" % (r,acc_no))

    my_db.commit()
    print("...transaction successful...")
#    main()

def Withdrawal():
    acc_no = input("Enter Account Number: ")
    description = input("Transaction type: ")
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
    key = str(ran)
    amt = int(input("Enter Withdraw Amount: "))
    dt = date.today()
    data_3 = (dt, description, key, amt, acc_no)
    sql_3 = ('insert into transaction(Date_time,Description,Reference,Amount,Account_Number) values(%s,%s,%s,%s,%s)')
#    a_1 = ("select Balance from transaction where Account_Number=%s")
#    q_1 = (acc_no)
    x = my_db.cursor()
    x.execute(sql_3,data_3)
    x.execute("select Balance from transaction where Account_Number=%s" % (acc_no))
    result = x.fetchone()
    r_1 =  result[0] - amt
#    sql_4 = ("update transaction set Balance where Account_Number=%s")
#    d_1 = (r_1,acc_no)
    x.execute("update transaction set Balance=%s where Account_Number=%s" % (r_1,acc_no))
    my_db.commit()
    print("...transaction successful...")
    main()

def List_all_Account():
    sql_5 = ('select * from account')
    x = my_db.cursor()
    x.execute(sql_5)
    result = x.fetchall()
    print(result)
    my_db.commit()
    main()

def List_all_Transactions():
    sql_6 = "select Date_time,Description,Reference,Amount,Balance from transaction"
    x = my_db.cursor()
    x.execute(sql_6)
    result = x.fetchall()
    print(result)
    my_db.commit()
    main()

def Display_Balance():
    acc_no = input("Enter Account Number: ")
    x = my_db.cursor()
    x.execute("select Balance from transaction where Account_Number=%s limit 1" % (acc_no))
    result = x.fetchone()
    print(result)
    my_db.commit()
    main()

def main():
    print(" 1. New Account\n 2. Deposit\n 3. Withdrawal\n 4. List all Accounts\n 5. List all Transactions\n 6. Display Balance")
    choice = input("Enter your choice: ")
    if choice == '1':
        New_Account()
    elif choice == '2':
        Deposit()
    elif choice == '3':
        Withdrawal()
    elif choice == '4':
        List_all_Account()
    elif choice == '5':
        List_all_Transactions()
    elif choice == '6':
        Display_Balance()

if __name__ == "__main__":
    main()

#...how to write a query account number to retrieve a data from table...    