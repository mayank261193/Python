# Drill 3: builds initials and a username from a messy full name.

full_name = "  asha   verma  "
birth_year = 1999

# YOUR CODE HERE
Clean=full_name.strip().title()
Name=Clean.replace("","")
Parts=Name.split()
Initials=Parts[0][0]+"."+Parts[1][0]+"."
print(Initials)
Username=Parts[0]+str(birth_year)[-2:]
print(Username)

# Expected:
# Initials: A.V.
# Username: asha99
