menu = {
    "Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50,
    "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00
    }

total_price = 0

while True:
    try:
        item = input('Item: ').title()
        if item in menu:
            total_price += menu.get(item)
            result = '$' + str(round(total_price, 1)) + '0'
            print('Total:', result)
    except KeyError:
        pass
    except EOFError:
        result = '$' + str(round(total_price, 1)) + '0'
        print('Total:', result)
        break
