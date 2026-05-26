print("=== unit converter ===")
value = float(input("enter value: "))
from_unit = input("from unit: ")
to_unit = input("to_unit: ")
#weight
if from_unit == "kg" and to_unit == "g":
  result = value * 1000
  print(result, "g") 
elif from_unit == "g" and to_unit == "kg":
 result = value / 1000
 print(result, "kg")
#temtperatue
elif from_unit == "c" and to_unit == "k":
 result = value + 273
 print(result, "k")
elif from_unit == "k" and to_unit == "c":
 result = value - 273
 print(result, "c")
#energy
elif from_unit == "j" and to_unit == "cal":
 result = value / 4.18
 print(result, "cal")
elif from_unit == "cal" and to_unit == "j":
 result = value * 4.18
 print(result, "j")
else:
  print("conversion not supported")