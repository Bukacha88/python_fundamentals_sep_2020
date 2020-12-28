items = input().split(', ')

data = input()


def collect(stash, i):
    if i not in stash:
        stash.append(i)
    return stash


def drop(stash, i):
    if i in stash:
        stash.remove(i)
    return stash


def combine(stash, old, new):
    if old in stash:
        stash.insert(stash.index(old) + 1, new)
    return stash


def renew(stash, i):
    if i in stash:
        stash.remove(i)
        stash.append(i)
    return stash


while not data == 'Craft!':
    command, item = data.split(' - ')
    if command == 'Collect':
        items = collect(items, item)
    elif command == 'Drop':
        items = drop(items, item)
    elif command == 'Combine Items':
        item = item.split(':')
        items = combine(items, item[0], item[1])
    elif command == 'Renew':
        items = renew(items, item)
    data = input()
print(", ".join(items))
