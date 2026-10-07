scores = [72, 81, 65, 90, 55, 43, 78]

# 1.
index = 0
for i in scores:
    index += 1

print(f"Number of students:", index)

# 2.
maximum = scores[0]
for i in scores:
    if i > maximum:
        maximum = i

print(f"Highest score:", maximum)


# 3.
lowest = scores[0]
for i in scores:
    if i < lowest:
        lowest = i

print(f"Lowest score:", lowest)


# 4.
s = 0
for i in scores:
    s = s + i

print(f"Total score:", s)


# 5.
x = 0
for i in scores:
    x+=1

print(f"Average score:", x)

"""Average is sum divided by frequency"""
avg = s / x
print(f"Average score:", avg)


""" Passing students """
number = 0
for i in scores:
    if i < 50:
        number += 1
passing = index - number

print(f"Passing students:", passing)


print(f"Failing students:", number)