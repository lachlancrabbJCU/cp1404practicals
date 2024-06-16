"""Files"""

# 1
user_name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()


# 2
in_file = open("name.txt", "r")
print(f"Hi {in_file.readline().strip()}!")
in_file.close()


# 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
result = first_number + second_number
print(f"{first_number} + {second_number} = {result}")


# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line.strip())
        total += number
print(f"total is {total}")
