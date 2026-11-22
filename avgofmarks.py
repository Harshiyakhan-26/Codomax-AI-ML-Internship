marks = [78, 85, 90, 66, 92]

total = 0
for m in marks:
    total += m

average = total / len(marks)
print("Marks:", marks)
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", average)
