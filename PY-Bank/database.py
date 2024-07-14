import mysql.connector as sql

mydb=sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='bank_management')
cursor=mydb.cursor()

def db_query(str):
	
	cursor.execute(str)
	result = cursor.fetchall()
	return result
		




def createcutomertable():


	cursor.execute('''
		create table customers(
		user_name varchar(20),
		password varchar(20),
		name varchar(20),
		age int,
		city varchar(20),
		account_number int,
		balance int,
		status blob)

		''') 

mydb.commit()

if __name__ == '__main__':
	createcutomertable()