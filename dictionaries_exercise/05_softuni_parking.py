number_of_commands = int(input())
data_base = {}
for _ in range(number_of_commands):
    data = input().split()
    if data[0] == 'register':
        if data[1] not in data_base:
            data_base[data[1]] = data[2]
            print(f"{data[1]} registered {data[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {data_base[data[1]]}")
    elif data[0] == 'unregister':
        if data[1] in data_base:
            data_base.pop(data[1])
            print(f"{data[1]} unregistered successfully")
        else:
            print(f"ERROR: user {data[1]} not found")
for key,value in data_base.items():
    print(f"{key} => {value}")