from bank import *
from register import *
print('WELCOME TO AJAY REDDY BANK ')

status=False

while True:
	try:
		register = int(input("1.sign-UP\n"
			                 "2.si IN \n "))
      
		if register==1 or register==2:
			if register==1:
				signup()
			if register==2:
				user=signin()
				status=True
				break
			
		else:
			print('ENTER THE VALID INPUT FROM THE ABOVE OPTIONS!!!!!!!!')




	except ValueError:
		print('INVALID INPUT TRY AGAIN!!!!!!!')

account_number=db_query(f'select account_number from customers where user_name="{user}"')


while status:
	try:
		fecility = int(input("1.BalanceEnquiry\n"
			                 "2.cash deposit \n "
			                 "3.cash withdraw\n"
			                 "4.Fund Transfer\n"))
      
		if fecility>=1 and  fecility<=4:
			if fecility==1:
				bobj=Bank(user,account_number[0][0])
				bobj.balancenquiry()
			elif fecility==2 :
				signin()
				break
			elif fecility==3:
				signin()
				break
			elif fecility==4 :
				signin()
				break	
		else:
			print('ENTER THE VALID INPUT FROM THE ABOVE OPTIONS!!!!!!!!')
	
	except ValueError:

		print('INVALID INPUT TRY AGAIN!!!!!!!')
