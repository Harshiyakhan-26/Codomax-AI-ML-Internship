fruits = ["apple", "banana", "mango"]

print(fruits[0])          # first item: apple
fruits.append("orange")   # add an item
fruits.remove("banana")   # remove an item
print(len(fruits))        # number of items

for fruit in fruits:
    print("I like", fruit)
