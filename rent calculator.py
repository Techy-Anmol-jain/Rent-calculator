print("                                                       Dividation of rent                    ")

rent = int(input("Enter amount of rent : "))
food = int(input("Enter amount of food expenditure : "))
electricity_expenditure = int(input("Enter amount of electricity consumed : "))
charge_per_unit = int(input("Enter the charge per unit : "))
persons = int(input("Enter the number of persons lived : "))
total_electricity_bill = electricity_expenditure*charge_per_unit
output = ( rent + food + total_electricity_bill )//persons
print("Each person will pay : ",output)
