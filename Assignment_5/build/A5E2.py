# Define food item prices as variables
cheeseburger = 4.99
bacon = 1.00
fries_w_gravy = 2.59
milkshake = 2.99

# Define the tax percentage as a variable
tax = 0.13

# Calculate subtotal, tax amount, and total
subtotal = cheeseburger + bacon + fries_w_gravy + milkshake
tax_amount = subtotal * tax
total = subtotal + tax_amount

# Print the receipt using the defined variables
print(f'''Food Item\tPrice
==========\t=======
Cheeseburger\t$ {cheeseburger:.2f}
+ Bacon\t\t$ {bacon:.2f}
Fries w/gravy\t$ {fries_w_gravy:.2f}
Milkshake\t$ {milkshake:.2f}
-------
Sub-total:\t$ {subtotal:.2f}
Tax ({tax*100:.0f}%):\t$ {tax_amount:.2f}
Total:\t\t$ {total:.2f}''')

