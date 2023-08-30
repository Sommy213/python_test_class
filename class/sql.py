import mysql.connector as sql
db = sql.connect(
    host ='localhost',
    user='root',
    password='sommy213####',
    database='ATTENENCE'
    )
cursor = db.cursor()
# cursor.execute('INSERT INTO student(FirstName,lastname,phonenumber)values("john","kiol","0904933")')
# db.commit()
cursor.execute('use ATTENENCE')
# cursor.execute('CREATE TABLE user (id INT PRIMARY KEY AUTO_INCREMENT,password INT,name VARCHAR(23))')
cursor.execute('INSERT INTO user (password,name)values(20322,"kate"),(29402,"gade"),(20292,"dage")')
cursor.execute('SELECT * FROM user WHERE id=1')
data = cursor.fetchall() 
print(data)