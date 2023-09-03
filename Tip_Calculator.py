# program to calculate cost of food after sales + fixed tip

# Create user input statement

food_cost = float(input('Please Enter the Charge For Your Food: '))

# Create variables to calculate tax and tip

tip = food_cost * 0.18
sales_tax = food_cost * 0.07
Total_cost = food_cost + tip + sales_tax

print('Hello, Welcome to Asanka! \n')
print('The tip is: $', (tip))
print('The sales tax is : $', (sales_tax))
print('The total amount for your food is : $', (Total_cost))