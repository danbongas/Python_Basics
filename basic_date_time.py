import calendar


print("Choose A Year & A Month:\n")
yr = int(input("Year: "))
mnth = int(input("Month: "))

print("\n")
cal = calendar.month(yr,mnth)

print("Resulting Calendar:\n")



print(cal)