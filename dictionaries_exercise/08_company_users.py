command = input()
companies_info = {}
while not command == 'End':
    company, employee_id = command.split(' -> ')
    if company not in companies_info:
        companies_info[company] = []
    if employee_id not in companies_info[company]:
        companies_info[company].append(employee_id)
    command = input()

for company_name, employee in sorted(companies_info.items(), key=lambda x: (x[0], x[1])):
    print(f"{company_name}")
    for e_id in employee:
        print(f"-- {e_id}")