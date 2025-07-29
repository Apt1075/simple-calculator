history = []

def calculaotr(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
         return num1 - num2
    elif operator == "*":
         return num1 * num2
    elif operator == "/":
         return num1 / num2
    elif operator == "%":
         return num1 % num2
    else:
        print("Invalid Operator")


while True:
    print("if you want to check hsitory type 'history' or if you want to exit type 'exit'")
    num1 = input("Enter the First Number: ")
    if num1 == "history":
        print(history)
        continue
    if num1 == "exit":
        break
    num2 = input("Enter the Second Number: ")
    if num2 == "history":
        print(history)
        continue
    if num2 == "exit":
        break
    operator = input("Enter the Operator +,-,*,/,% : ")
    if operator == "history":
        print(history)
        continue
    if operator == "exit":
        break
    result =  calculaotr(int(num1),int(num2),operator)
    print(f"num1 {operator} num2 = {result}")
    history.append(f"{num1} {operator} {num2} = {result}")



  
   
     