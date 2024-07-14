 
from database import *
import datetime
class Bank:
	def __init__(self,username,password):
		self.__username=username
		self.__password=password


	def create_transaction_table(self):
		db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")

	def balancenquiry(self):
		temp=db_query(f"SELECT balance from customers WHERE user_name='{self.__username}';")
		print(f'{self.__username} balance is {temp[0][0]}')

			
	def deposite(self,amount):
		temp=db_query(f"SELECT balance from customers WHERE user_name='{self.__username}';")
		test=temp[0][0]+amount

		

