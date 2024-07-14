
from bank import *
from customer import *
import random

from customer import *
def signup():
	username=input('enter the username:')
	temp=db_query(f'select user_name from customers where user_name="{username}";')
	if temp:
		print('USERNAME is not available')
		signup()
		
	else:
		print('username available please procceed')

		password=input('enter the password: ')
		name=input('enter the name: ')
		age=int(input('enter the age: '))
		city=input('enter the city: ')
		while True:
			account_number=random.randint(10000000,99999999)
			temp=db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
			if temp:
				continue
			else:
				print('account number is',{account_number})
				break

	cobj=Customer(username,password,name,age,city,account_number)
	cobj.createuser()
	bobj=Bank(username,account_number)
	bobj.create_transaction_table()


def signin():
	username=input('enter the username:')
	temp=db_query(f'select user_name from customers where user_name="{username}";')

	if temp:
		while True:
			password=input('enter the password:')
			temp=db_query(f'select password from customers where user_name="{username}";')

			if temp[0][0]==password:

				print('Sig in sucessfully')
				return username
			else:
				print('enter valid password')
				continue
	else:
		print('enter the valid username')
		signin()


	



