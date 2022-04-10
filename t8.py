import mysql.connector
import re   

password = input('please enter your password:  ')

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='t8')         





cursor = cnx.cursor()  
  
def check(email):   
    if(re.search(regex,email)):   
        cursor.execute('INSERT INTO up VALUES (\'%s\', \'%s\')' % (email, password))
        cnx.commit()
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
      
    email = input('please enter your email :   ')  
    check(email)   


cnx.close()