print (""" ##### Welcome to my #######
#####  basic converter #####
    1.Kg to Lbs
    2.Lbs to Kg
    3.L to ml
    4.ml to L
##################################### """)
choice = int(input('What would you like to covert?:  '))
if choice == 1:
    unit = int(input('Write Kg to convert to Lbs: '))
    converted = unit * 2.205
    print(f"Result: {converted} Lbs")
elif choice == 2:
    unit = int(input('Write Lbs to convert to Kg: '))
    converted = unit / 2.205
    print(f"Result: {converted} Kg")
elif choice == 3:
    unit = int(input('Write L to convert to mL: '))
    converted = unit * 1000
    print(f"Result: {converted} mL")
else:
    unit = int(input('Write mL to convert to L: '))
    converted = unit / 1000
    print(f"Result: {converted} L")
