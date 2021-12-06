import mysql.connector
import os
import smtplib
from datetime import date

# Current year plus one. When a year is entered for a vehicle
# it must be equal to or lower than this number.
DATE = date.today()
YEAR = DATE.year + 1



# Establish a conneciton to the database.
MYDB = mysql.connector.connect(
	host = "localhost",
	user = 'testuser',
	passwd = 'Jb=<4,Xfk;twS*Zh',
	database = "cartrack",
)

# Global variables for sending the emails
SENDER_EMAIL = "pythonemail89@gmail.com"
EMAIL_PASS = os.environ.get("EMAIL_PASSWORD")
SERVER = smtplib.SMTP('smtp.gmail.com', 587)

SERVER.starttls()


# For testing purposes the salesperson password is 'sales'
# and the inventory manager password is 'inventory'

def main():
	# Greet the user
	print()
	print('Welcome to Cartrack')
	print()

	# Start the login screen.
	log_in()

	# Close mysql connection.
	print()
	print("Closing mysql connection")
	MYDB.close()
	print("mysql connection closed.")

	print()
	print("Exiting program")



def log_in():
	# Notifiy the user they can enter q to quit back to the login screen
	print("Entering 'q' while at the login screen will end the program.")
	print("Entering 'q' in another menu will quit back to the login screen.")
	print('----------------------------------------------------------')

	# Ask the user if they are loggin in as a salesperson or 
	# inventory manager.
	print('Salesperson or Inventory Manager?')
	print("Enter 's' for Salesperson or 'i' for Inventory Manager")
	choice = input('Login: ')

	# Input validation loop to make sure the user enters a valid option.
	while choice.lower() != 's' and choice.lower() != 'i' and \
	choice.lower() != 'q':
		choice = input('Error. Must enter a valid option. s, i, or q: ')

	# If 's' verify the password and if correct start the salesperson
	# function.
	if choice.lower() == 's':
		password = input('Password: ')
		while password != 'sales' and password != 'q':
			print('The password you entered is incorrect.')
			password = input('Re-enter the password: ')

		if password == 'q':
			return


		print()
		print('Login successful.')
		print('-----------------')
		salesperson()


	# If 'i' verify the password and if correct start the inventory
	# function.
	if choice.lower() == 'i':
		password = input('Password: ')
		while password != 'inventory' and password != 'q':
			print('The password you entered is incorrect.')
			password = input('Re-enter the password: ')

		if password == 'q':
			return
			
		print()
		print('Login successful.')
		print('-----------------')
		inventory()


	# If 'q' then return to the main function ending the program.
	if choice.lower() == 'q':
		return


def salesperson():
	print()

	# Menu options for salesperson.
	print('------------------------')
	print('1. Search vehicles')
	print('2. Search customers')
	print('3. Add new customer')
	print('4. Update customer information')
	print('5. Remove customer')
	print("Enter 'q' to return to the login screen")

	# Get the salesperson's choice.
	choice = input('Enter: ')
	print()

	# Validation loop to ensure a valid option was chosen.
	while choice != '1' and choice != '2' and choice != '3' \
	and choice != '4' and choice != '5' and choice.lower() != 'q':
		print('Invalid input')
		choice = input("Enter 1 through 5 or 'q' to quit: ")


	# Determine which option was chosen and call the 
	# related function.
	if choice == '1':
		salesSearchVehicles()
	elif choice == '2':
		salesSearchCust()
	elif choice == '3':
		salesAddCust()
	elif choice == '4':
		salesUpdateCust()
	elif choice == '5':
		salesRemoveCust()
	elif choice.lower() == 'q':
		log_in()

	




def salesSearchVehicles():
	print()

	# Ask the salesperson for the make and model of the vehicle
	# they are searching for.
	make = input('Enter the make: ')
	model = input('Enter the model: ')

	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM vehicles WHERE make = %s AND model = %s"

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql, (make, model))
	my_result = my_cursor.fetchall()

	# Check to see if any results are found. If not tell the user.
	# Otherwise display the results.
	if my_cursor.rowcount == 0:
		print('No results found')
	else:
		# Print column names for the vehicles table.
		print('| ID | Make | Model | Year | Price | Quantity')
		# Print the search results.
		for row in my_result:
			print(row)

	

	# Send the user back to the salesperson menu.
	salesperson()




	


def salesSearchCust():
	print()

	# Ask the salesperson for the first and last name of the
	# customer they are searching for.
	first = input('Enter the first name: ')
	last = input('Enter the last name: ')

	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM customer WHERE first_name = %s AND last_name = %s"

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql, (first, last)) 
	my_result = my_cursor.fetchall()
	print()

	# Check to see if any results are found. If not tell the user.
	# Otherwise display the results.
	if my_cursor.rowcount == 0:
		print('No results found')
	else:
		# Print colunm names for the customer table
		print('| ID | First Name | Last Name | Make | Model | Year | Phone# | Sales ID')
		# Print the search results.
		for row in my_result:
			print(row)

	# Send the user back to the salesperson menu.
	salesperson()




def salesAddCust():
	print()

	# Ask the salesperson for the customers info to add to 
	# the database.
	first = input("Enter the customer's first name: ")
	last = input("Enter the customer's last name: ")
	make = input("Enter the make of the vehicle the customer is looking for: ")
	model = input("Enter the model of the vehicle the customer is looking for: ")
	year = validateYear("Enter the year of the vehicle the customer is looking for: ")
	phone = validatePhone("Enter the customer's phone number: ")
	sales_id = validateInteger("Enter your sales id number: ")

	# Create a cursor, a variable to hold the sql command and a variable to hold
	# the user entered values.
	my_cursor = MYDB.cursor()
	sql = "INSERT INTO customer (first_name, last_name, make, model, year, phone, idsales) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	val = (first, last, make, model, year, phone, sales_id)

	# Execute the sql command and commit the to the database.
	my_cursor.execute(sql, val)
	MYDB.commit()
	print()

	# Inform the user that the record was added successfully.
	print("Customer added.")

	# Send the user back to the salesperson menu.
	salesperson()




def salesUpdateCust():
	print()

	# Ask the salesperson for the id number of the customer they wish to update.
	cust_id = validateInteger("Enter the customer's id number: ")
	
	# Search to make sure the customer exists before attempting to update.
	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM customer WHERE idcustomer = %s"

	# Execute the sql command save the results to my_result
	my_cursor.execute(sql, (cust_id,))
	my_result = my_cursor.fetchall()

	# Check to see if any results are found. If not tell the user.
	# Otherwise update the customer record.
	if my_cursor.rowcount == 0:
		print('No customer found')
	else:
		# Print the search result so the salesperson can verify they have
		# the correct customer.
		print(my_result)

		# Ask the salesperson which category to update
		print('------------------------')
		print('1. First name')
		print('2. Last name')
		print('3. Make')
		print('4. Model')
		print('5. Year')
		print('6. Phone')
		print("Enter 'q' to return to the Sales menu")
		choice = input("Enter the category you wish to update: ")

		# Loop to continue updating until they enter 'q'
		while choice.lower() != 'q':
			# Validation loop to ensure a valid option was chosen.
			while choice != '1' and choice != '2' and choice != '3' \
			and choice != '4' and choice != '5' and choice.lower() != '6' \
			and choice.lower() != 'q':
				print('Invalid input')
				choice = input("Enter 1 through 6 or 'q' to quit: ")

			# If '1' was entered update the first name.
			if choice.lower() == '1':
				# Ask the salesperson for the new value.
				new_first = input("Enter the customer's new first name: ")
				# New sql command.
				sql = "UPDATE customer SET first_name = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_first, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()

			# If '2' was entered update the last name.
			elif choice.lower() == '2':
				# Ask the salesperson for the new value.
				new_last = input("Enter the customer's new last name: ")
				# New sql command.
				sql = "UPDATE customer SET last_name = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_last, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()

			# If '3' was entered update the make of the vehicle
			# the customer is looking for.
			elif choice.lower() == '3':
				# Ask the salesperson for the new value.
				new_make = input("Enter the make of the vehicle: ")
				# New sql command.
				sql = "UPDATE customer SET make = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_make, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()

			# if '4' was entered update the model of the vehicle
			# the customer is looking for.
			elif choice.lower() == '4':
				# Ask the salesperson for the new value.
				new_model = input("Enter the model of the vehicle: ")
				# New sql command.
				sql = "UPDATE customer SET model = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_model, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()

			# If '5' was entered update the year of the vehicle
			# the customer is looking for.	
			elif choice.lower() == '5':
				# Ask the salesperson for the new value.
				new_year = validateYear("Enter the year of the new vehicle: ")
				# New sql command.
				sql = "UPDATE customer SET year = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_year, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()

			# If '6' was entered update the phone number.
			elif choice.lower() == '6':
				# Ask the salesperson for the new value.
				new_phone = validatePhone("Enter the customer's new phone number: ")
				# New sql command.
				sql = "UPDATE customer SET phone = %s WHERE idcustomer = %s"

				# Execute the update command and then commit it.
				my_cursor.execute(sql, (new_phone, cust_id))
				MYDB.commit()
				print()

				# Inform the salesperson upon successful update.
				print("Customer information successfully updated.")
				print()


			# Ask the salesperson what they would like to update next
			choice = input("Enter the next category to update or 'q' to quit: ")

		

	# Send the user back to the salesperson menu.
	salesperson()




def salesRemoveCust():
	print()

	# Ask the salesperson for the first and last names of the customer they wish to remove.
	first = input("Enter the first name of the customer to be removed: ")
	last = input("Enter the last name of the customer to be removed: ")

	# Search to make sure the customer exists before attempting to delete.
	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM customer WHERE first_name = %s AND last_name = %s"

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql, (first, last)) 
	my_result = my_cursor.fetchall()

	# Check to see if any results are found. If not tell the user.
	# Otherwise remove the customer record.
	if my_cursor.rowcount == 0:
		print('No customer found')
	else:
		# Command to delete the customer row from the table
		sql = "DELETE FROM customer WHERE first_name = %s AND last_name = %s"
		my_cursor.execute(sql, (first, last))
		MYDB.commit()
		print()

		# Inform the salesperson that the customer was successfully deleted
		print("Customer removed.")

	# Send the user back to the salesperson menu.
	salesperson()





def inventory():
	print()

	# Menu options for inventory management.
	print('------------------------')
	print('1. Show all current vehicles')
	print('2. Search vehicles')
	print('3. Add new vehicle')
	print('4. Remove vehicle')
	print("Enter 'q' to return to the login screen")

	# Get the salesperson's choice.
	choice = input('Enter: ')
	print()

	# Validation loop to ensure a valid option was chosen.
	while choice != '1' and choice != '2' and choice != '3' \
	and choice != '4' and choice.lower() != 'q':
		print('Invalid input')
		choice = input("Enter 1 through 4 or 'q' to quit: ")


	# Determine which option was chosen and call the 
	# related function.
	if choice == '1':
		invShowAll()
	elif choice == '2':
		invSearchVehicles()
	elif choice == '3':
		invAddVehicles()
	elif choice == '4':
		invRemoveVehicles()
	elif choice.lower() == 'q':
		log_in()




def invShowAll():
	print()

	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = 'SELECT * FROM VEHICLES'

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql)
	my_result = my_cursor.fetchall()

	# Print column names for the vehicles table.
	print('|  ID  |  Make  |  Model  |  Year  |  Price  |  Quantity  |')
	# Print sql command results.
	for x in my_result:
		print(x)

	# Send the user back to the inventory menu.
	inventory()




def invSearchVehicles():
	print()

	# Ask the inventory manager for the make and model of the
	# vehicle they are searching for.
	make = input('Enter the make: ')
	model = input('Enter the model: ')

	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM vehicles WHERE make = %s AND model = %s"

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql, (make, model)) 
	my_result = my_cursor.fetchall()

	# Check to see if any results are found. If not tell the user.
	# Otherwise display the results.
	if my_cursor.rowcount == 0:
		print('No results found')
	else:
		# Print colunm names for the vehicles table
		print('|  ID  |  Make  |  Model  |  Year  |  Price  |  Quantity  |')
		# Print the search results.
		for row in my_result:
			print(row)

	# Send the user back to the inventory menu.
	inventory()


def invAddVehicles():
	print()

	# Ask the inventory manager for the make, model, year, price and quantity
	# of the vehicle they are adding
	make = input('Enter the make: ')
	model = input('Enter the model: ')
	year = validateYear('Enter the year: ')
	price = validateInteger('Enter the price: ')
	quant = validateInteger('Enter the quantity to add: ')

	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor(buffered=True)
	sql = "SELECT * FROM vehicles WHERE make = %s AND model = %s AND year = %s AND price = %s"

	# Search the vehicles database to verify if this vehicle
	# already exists.
	my_cursor.execute(sql, (make, model, year, price)) 
	my_result = my_cursor.fetchall()

	# Add the vehicle if it does not already exist.
	if my_cursor.rowcount == 0:
		# New sql command to add the vehicle
		sql = "INSERT INTO vehicles (make, model, year, price, quantity) VALUES (%s, %s, %s, %s, %s)"
		val = (make, model, year, price, quant)

		# Execute the sql command and commit the to the database.
		my_cursor.execute(sql, val)
		MYDB.commit()
		print()

		# Search the customer database to see if this vehicle matches the make and model of 
		# any vehicles that customers are looking for and if so send an email to the
		# salesperson notifiying them that this new vehicle may match the vehicle a 
		# customer is looking for.
		
		# New sql command to search the customer database to see if the added
		# vehicle matches a vehicle a customer is looking for.
		sql = "SELECT idcustomer FROM customer WHERE make = %s AND model = %s"

		# Execute the sql command and save the results.
		my_cursor.execute(sql, (make, model)) 
		my_result = my_cursor.fetchall()

		# Save the customer IDs into a list
		cust_ids =[]
		for row in my_result:
			customer = int(row[0])
			cust_ids.append(customer)


		# Save the amount of rows retrieved to a variable
		rows = my_cursor.rowcount

		# Close the cursor.
		my_cursor.close()

		# Check to see if any matches were found. If so send an email to the 
		# relevant salesperson to notify them of the customers who should be 
		# contacted about the new vehicle added.
		
		
		for i in range(len(cust_ids)):
			# New cursor
			my_cursor = MYDB.cursor(buffered=True)

			# New sql command to retrieve and save the first name of the customer.
			sql = "SELECT first_name FROM customer WHERE make = %s AND model = %s AND idcustomer = %s"

			# Execute the command and save the results.
			my_cursor.execute(sql, (make, model, cust_ids[i]))
			my_result = my_cursor.fetchone()
			first = str(my_result[0])

			# New sql command to retrieve and save the last name of the customer.
			sql = "SELECT last_name FROM customer WHERE make = %s AND model = %s AND idcustomer = %s"

			# Execute the command and save the results.
			my_cursor.execute(sql, (make, model, cust_ids[i]))
			my_result = my_cursor.fetchone()
			last = str(my_result[0])

			# New sql command to retrieve and save the ID of the salesperson.
			sql = "SELECT idsales FROM customer WHERE make = %s AND model = %s AND idcustomer = %s"

			# Execute the command and save the results.
			my_cursor.execute(sql, (make, model, cust_ids[i]))
			my_result = my_cursor.fetchone()
			sales_id = int(my_result[0])

			# New sql command to retrieve and save the email address
			# of the salesperson
			sql = "SELECT email FROM sales WHERE idsales = %s"
			
			# Execute the command and save the results.
			my_cursor.execute(sql, (sales_id,))
			my_result = my_cursor.fetchone()
			sales_email = str(my_result[0])

			# Login to the email account
			SERVER.login(SENDER_EMAIL, EMAIL_PASS)

			# Create the message to send to the salesperson
			message = "\nA " + make + " " + model + " was added to inventory. " + first + " " + last + ", " + "ID: " + str(cust_ids[i]) + " is looking for a similar vehicle."

			# Send an email to the salesperson.
			SERVER.sendmail(SENDER_EMAIL, sales_email, message)

			# Close the cursor
			my_cursor.close()



		# Inform the user that the record was added successfully.
		print("Vehicle added.")

	# Update the vehicle quantity if it already exists.
	else:
		# New sql command to return only the quantity.
		sql = "SELECT quantity FROM vehicles WHERE make = %s AND model = %s AND year = %s AND price = %s"

		# Execute the command and save the result.
		my_cursor.execute(sql, (make, model, year, price))
		quant_result = my_cursor.fetchone()

		# Save the original quantity to a variable.
		old_quant = int(quant_result[0])

		# Save the old quantity amount + the amount to be added to a new variable.
		new_quant = old_quant + quant

		# New sql command to update the quantity.
		sql = "UPDATE vehicles SET quantity = %s WHERE make = %s AND model = %s AND year = %s AND price = %s"

		# Execute the command and commit it.
		my_cursor.execute(sql, (new_quant, make, model, year, price))
		MYDB.commit()
		print()
		
		# Inform the user that the record was added successfully.
		print("Vehicle added.")

	# Send the user back to the inventory menu.
	inventory()




def invRemoveVehicles():
	print()

	# Ask the inventory manager for the make, model, and year
	# of the vehicle they wish to remove.
	make = input("Enter the make of the vehicle to be removed: ")
	model = input("Enter the model of the vehicle to be removed: ")
	year = validateYear("Enter the year of the vehicle to be removed: ")

	# Search to make sure the vehicle exists before attempting to delete.
	# Create a cursor and a variable to hold the sql command.
	my_cursor = MYDB.cursor()
	sql = "SELECT * FROM vehicles WHERE make = %s AND model = %s AND year = %s"

	# Execute the sql command and save the results to my_result.
	my_cursor.execute(sql, (make, model, year)) 
	my_result = my_cursor.fetchall()

	# Check to see if any results are found. If not tell the user.
	# Otherwise remove or update the record.
	if my_cursor.rowcount == 0:
		print('No vehicle found')

	# If the vehicle does exist display the quantity to the user and
	# ask how many they wish to remove then either update the quantity
	# or delete the record depending on the user input.
	else:
		# New sql command to return only the quantity.
		sql = "SELECT quantity FROM vehicles WHERE make = %s AND model = %s AND year = %s"

		# Execute the command and save the result.
		my_cursor.execute(sql, (make, model, year))
		quant_result = my_cursor.fetchone()

		# Save the original quantity to a variable.
		old_quant = int(quant_result[0])
		print()

		# Notify the user of the quanitity and ask them how many to remove.
		print("There are currently " + str(old_quant) + " of this vehicle in inventory.")
		remove_quant = validateInteger("Enter the amount you wish to remove: ")

		# Validation loop so the user enters a valid number for the quantity
		# they wish to remove.
		while remove_quant < 0 and remove_quant > old_quant:
			print("You must enter a quantity greater than 0 and less than or")
			remove_quant = validateInteger("equal to the current quantity: ")

		# If the amount they wish to remove is less then the amount in inventory
		# update the quantity.
		if remove_quant < old_quant:
			# Variable to hold the new quantity once the correct amount is removed.
			new_quant = old_quant - remove_quant

			# New sql command to update the quantity
			sql = "UPDATE vehicles SET quantity = %s WHERE make = %s AND model = %s AND year = %s"

			# Execute the update command and then commit it.
			my_cursor.execute(sql, (new_quant, make, model, year))
			MYDB.commit()
			print()

			# Inform the salesperson upon successful update.
			print("Vehicle quantity successfully updated.")
			print()

		# If the amount they wish to remove is equal to the current quantity
		# then delete the record.
		else:
			# Command to delete the vehicle from the table
			sql = "DELETE FROM vehicles WHERE make = %s AND model = %s AND year = %s"
			my_cursor.execute(sql, (make, model, year))
			MYDB.commit()
			print()

			# Inform the user that the vehicle was successfully deleted
			print("Vehicle removed.")



	# Send the user back to the inventory menu.
	inventory()


def validateYear(prompt):
	# Validation loop to ensure a valid year is entered.
	while True:
		# Get the input from the user.
		try:
			year = int(input(prompt))
		# If the input is the wrong type continue the loop.
		except ValueError:
			print()
			print('Year must be an integer.')
			continue

		# If the year is too low or too high continue the loop
		if year <= 1970 or year > YEAR:
			print()
			print('Year must be greater than 1970 and less')
			print('than the next year.')
			continue
		# If valid input is entered break the loop.
		else:
			break

	# Return the year back to the function that called it.
	return year


def validatePhone(prompt):
	# Validation loop to ensure a valid phone # is entered.
	while True:
		# Get the input from the user.
		try:
			phone = int(input(prompt))
		# If the input is the wrong type continue the loop.
		except ValueError:
			print()
			print('Phone # must be an integer.')
			continue

		# If the phone # is not 10 digits continue the loop.
		if len(str(phone)) != 10:
			print()
			print('Phone # must be a 10 digit integer.')
			continue
		# If the phone # is valid break the loop.
		else:
			break

	# Return the phone number back to the function that called it.
	return phone


def validateInteger(prompt):
	# Validation loop to ensure a valid ID # is entered.
	while True:
		# Get the input from the user.
		try:
			id_num = int(input(prompt))
		# If teh input is not an integer continue the loop.
		except ValueError:
			print()
			print('# must be an integer')
			continue

		# If the number is negative continue the loop.
		if id_num < 0:
			print()
			print('# cannot be negative')
			continue
		# If the number is valid break the loop.
		else:
			break

	# Return the id number to the function that called it.
	return id_num
	


main()