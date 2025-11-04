print("---------------- Rent Calculator ----------------")
# Rent Calculator
rent = int(input("Enter the monthly rent amount (R): "))
water = float(input("Enter the monthly water bill amount (R): "))
electricity = int(input("Enter the monthly electricity bill amount (R): "))
groceries = float(input("Enter the monthly groceries amount (R): "))
person = int(input("Enter the number of people sharing the rent: "))
# Calculations
grand_total = rent + water + electricity + groceries
total_rent_per_person = (rent) / person
utilities_per_person = (water + electricity) / person
groceries_per_person = (groceries) / person   
# Output
print("--------------------------------------------------")
print("Grand Total Monthly Cost: R{:.2f}".format(grand_total))
print("--------------------------------------------------")
print("Total Rent per Person: R{:.2f}".format(total_rent_per_person))
print("Utilities per Person: R{:.2f}".format(utilities_per_person))
print("Groceries per Person: R{:.2f}".format(groceries_per_person))
print("--------------------------------------------------")

print("Thank you for using the Rent Calculator!")

  
