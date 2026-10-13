nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, end="")

for num in nums:
    if num == 3:
        print(f"{num} is found")
        break
    print(num)

for num in nums:
    if num == 4:
        print(f"{num} is found")
        continue
    print(num)

for num in nums:
    for letter in "abcde":
        print(f"{num} and {letter}")

for num in range(1, 11):
    print(num)

num = 10
while num > 0:
    if num == 4:
        break
    print(num)
    num -= 1
