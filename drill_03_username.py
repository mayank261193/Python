# Drill 3: builds initials and a username from a messy full name.

full_name = "  asha   verma  "
birth_year = 1999

# YOUR CODE HERE
Clean=full_name.strip().title()           #Assign the value to clean and removing spaces.
Name=Clean.replace("","")                 #Assign Name and removing middle spaces.
Parts=Name.split()                        #Split the Name into parts like array.
Initials=Parts[0][0]+"."+Parts[1][0]+"."  #Calling of particular values.
print(Initials)# Print initials.
Username=Parts[0]+str(birth_year)[-2:]    #Creating username by calling particular part using concatenation
print(Username)

# Expected:
# Initials: A.V.
# Username: asha99
