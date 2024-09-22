colors = ["blue", "red", "green","red","pink","purple","blue","blue","yellow","red","pink","orange"]
print(len(colors))
print(colors.count("blue"))
colors.append("white")
print(colors)


print("purple" in colors)
print("black" in colors)

print("purple" not in colors)
print("black" not in colors)

colors.remove("red")
print(colors)

colors.reverse()
print(colors)


print(colors.index("green"))
print(colors[10])

print(colors.index("purple"))
print(colors[7])

print(colors[0:3])
colors.reverse()
print(colors[4:9])

print(colors[-1])

colors[11] = "black"
print(colors)


