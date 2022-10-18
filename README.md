# Cartrack
My Software Techonology program capstone project Cartrack.

Section 1: Login Screen

Upon starting Cartrack you will be presented with a login screen and three options.

Enter ‘q’ to quit the program
Enter ‘s’ to be presented with the salesperson menu
Enter ‘i’ to be presented with the inventory management menu

	Choosing options 2 or 3 will require you to enter the relevant password. For testing purposes the password for option 2 is ‘sales’ and the password for option 3 is ‘inventory’

Section 2: Salesperson Menu
	
	If the sales option was chosen at the login screen you will be presented with 6 options.

Search vehicles
Search customers
Add new customer
Update customer information
Remove customer
Enter ‘q’ to return to the login screen

Section 2.1: Search vehicles

	The search vehicles option is available for a salesperson to search for a vehicle that one of their customers is interested in to see if that vehicle is available. You will be prompted to enter the make and model of the vehicle you are searching for and will be presented with all matching vehicles currently in inventory and then returned to the sales menu.

Section 2.2: Search customers

	The search customers option is for salespeople to be able to search for customers that have been previously entered into the system to give them information necessary for options 4 or 5 or to be able to contact the customer. You will be prompted to enter the customer’s first and last name and will be presented with all matching customers and their information.

Section 2.3: Add new customer

	The Add new customer option is for salespersons meeting with a new customer. The salesperson will be prompted to enter the customers first and last name, make, model and year of the vehicle they are looking for, the customer’s phone number, and your sales id. The customer information will be saved in the database for future reference.

Section 2.4: Update customer information

	The Update customer information option is available for a salesperson to change a customer's information if their desired vehicle changes or if they have their name changed or recieve a new phone number.You will be asked to enter the customer’s id number and it will display the customer’s information so that you can verify the right customer has been selected. You will be presented with 6 options or you can enter ‘q’ to return to the previous menu.

First name
Last name
Make
Model
Year
Phone
	
	After choosing one of the options you will be asked for the new information and then you will be returned to the category menu. 

Section 2.5: Remove customer

	If the remove customer option is chosen you will be asked for the first and last name of the customer and then the customer will be removed from the system. It is advised to use the search customer option first to verify that you have the correct customer before choosing the remove customer option.

Section 3: Inventory management menu

	If the inventory option was chosen at the login screen you will be presented with the inventory management menus which will present you with 4 options or ‘q’ can be entered to return to the login screen.

Show all current vehicles
Search vehicles
Add new vehicle
Remove vehicle

Section 3.1: Show all current vehicles

	If option 1 was chosen you will be presented with a list of all vehicles currently in inventory including the id, make, model, year, price and quantity of that vehicle.

Section 3.2: Search vehicles
	
	If option 2 was chosen you will be asked for the make and model of the vehicle and then presented with a list of all matching vehicles along with the id, make, model, year, price and quantity of that vehicle.

Section 3.3: Add new vehicle

	If option 3 was chosen you will be asked for the make, model, year and price of the vehicle as well as the quantity being added to inventory. This function will search to see if this vehicle already exists and if so will only update the quantity otherwise it will add a new vehicle record, because of this the inventory manager will not have to search for each vehicle before adding it to make sure it does not already exist. This will prevent multiple records for the same vehicle. 

	This function will also search the customer database when a new vehicle is entered and if the make and model of the added vehicle matches the make and model of a vehicle from the customer database an email will be sent to the salesperson whose id was matched with the customer upon adding them to the database. This email will notify the salesperson that a vehicle similar to what that customer is looking for has been added to inventory.

Section 3.4: Remove vehicle

	If option 4 was chosen you will be asked for the make, model and year of the vehicle you wish to remove from inventory. The vehicle will be searched for and if it exists you will be notified of the quantity of that vehicle that is currently in inventory and asked how many are to be removed. If you choose to remove less than the quantity that is in inventory the quantity of that vehicle will be updated, otherwise the record for that vehicle will be removed from the database.
