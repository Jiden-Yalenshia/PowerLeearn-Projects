print("------------Welcome to my calculator ------------------------ ")
operator=input("Please insert the operator you want to work with")
f_num=float(input("Please insert the first number"))
s_num=float(input("Please insert the second number"))

if operator == "+" :
  print(f_num + s_num)
if operator == "-" :
  print(f_num - s_num)
if operator == "*" :
  print(f_num * s_num)  
if operator == "/" :
  print(f_num / s_num)    