# incrementing loop (basic for), from zero to 10 (10). or start index! (5, 10) it runs till 9. 10th index in the range, starting with 5. (0,10,2) 2: steps! so 0,2,4,6,8.

for i in range(0, 10, 2):
    print(i)

# for each loop

array = ["Hello", ",", "world", "!!!"]

# for item in array:
#    print(item)


# print("0", array(0))
# print("2", array(2))

# for i in range(len(array) - 1):
#    print(array[i])

# while loop, condition, infinite loop, we will get stuck :D it is not commonly used


index = 0
count = 10
while index < count:
    print(index)

    index += 1

# this will start with 0, end at 9

# while True:
#    print("Hello World", flush=True)


for i in range(10):
    if i == 2:
        continue  # the second index won't be printed

    print(i)

    if i == 5:  # runs till 5 only
        break

# not case sensitive, I could pass spaces as well, like "name ". underscores can be used! like: my_name

users = [
    {
        "name ": "Jelen",
        "age": 26,

    },
    {
        "my_name": "Santa Claus",
        "age": "9999",
    }
]

for user in users:
    try:

        print("Name:", user["name"])

    except KeyError as error:
        print("KeyError:", error)

        print("Name:", user["my_name"])

# except Exception:
#    pass


# stackoverflow