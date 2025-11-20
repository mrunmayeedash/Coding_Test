#Program 3
a = int(input("Enter a number: "))
limit = a if a % 2 != 0 else a - 1

result = []
for i in range(limit):
    result.append(2 * i + 1)

print("Output:", result)
