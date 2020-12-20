number_tab = int(input())
salary = int(input())

for i in range(1, number_tab +1 ):
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
else:
    print(salary)
