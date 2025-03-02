

year = int(input("Enter your year of birth: "))

if year >= 1901 and year <= 1927:
    print("Greatest Generation")
    print("You are 98 years plus.")
    print()
elif year >= 1928 and year <= 1945:
    print("Silent Generation")
    print("You are 80 years plus.")
    print()
elif year >= 1946 and year <= 1964:
    print("Baby Boomers")
    print("You are 63 years plus.")
    print()
elif year >= 1965 and year <= 1980:
    print("Generation X")
    print("You are 48 years plus.")
    print()
elif year >= 1981 and year <= 1996:
    print("Millennials")
    print("You are 32 years plus.")
    print()
elif year >= 1997 and year <= 2012:
    print("Generation Z")
    print("You are 17 years plus.")
    print()
elif year >= 2013 and year <= 2025:
    print("Generation Alpha")
    print("You are 5 years plus.")
    print()
else:
    print("Invalid year of birth! Please enter a valid year.")
    print()


