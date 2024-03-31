gros_list = {}

while True:
    try:
        item = input()
        if item not in gros_list:
            gros_list.setdefault(item, 1)
        else:
            gros_list[item] += 1
    except KeyError:
        pass
    except EOFError:
        for key, value in sorted(gros_list.items()):
            print(value, key.upper())
        break
