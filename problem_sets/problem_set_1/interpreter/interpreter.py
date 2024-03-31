x, y, z = input("Write: ").split(" ")
x, z = int(x), int(z)
if y == "+":
    final = float(x + z)
elif y == "-":
    final = float(x - z)
elif y == "*":
    final = float(x * z)
else:
    final = float(x / z)
print(final)
