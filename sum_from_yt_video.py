first = 10.1
second = 20
sum: 30.1 #expected result

sum = (first + second)
print("Sum: " + str(sum))


# or could be:
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

#or could be:
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))