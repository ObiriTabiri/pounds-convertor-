print(""" CURENCY YOU CAN CONVERT TO DOLLARS ARE
      POUNDS
      FRANCS
      MARKS
      LIRE
      """)

pounds = 0
francs = 0
marks = 0
lire = 0 

Money_converter = input("What curency you want to convert: ")
amount_converter = input("how much would like to convert: ")

 
if Money_converter == pounds:
    amount = amount_converter * 1.15
     
elif Money_converter == francs:
    amount = amount_converter * 1
elif Money_converter == marks:
    amount =amount_converter * 0.506477
elif Money_converter == lire:
    amount = amount_converter * 0.054
else:
    print("Input Is Not Recognized")
    
print(amount)