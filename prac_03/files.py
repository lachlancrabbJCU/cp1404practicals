"""Files"""

# 1
name = input("Name: ")
out_file = open(f"{name}.txt", "w")
print(name, file=out_file)
out_file.close()


# 2
in_file = open(f"{name}.txt", "r")
print(f"Hi {in_file.readline().strip()}!")
in_file.close()


# 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline().strip())
    second_number = int(in_file.readline().strip())
print(first_number + second_number)


# 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line.strip())
    total += number
print(f"total is {total}")
