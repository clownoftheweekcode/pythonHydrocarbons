carbons = input("how many carbons are there? (ex: c4 is 4 carbons)\n")
if carbons == "1":
    carbonNum = "meth"
elif carbons == "2":
    carbonNum = "eth"
elif carbons == "3":
    carbonNum = "prop"
elif carbons == "4":
    carbonNum = "but"

bond = input("what is the highest bond in numbers? (ex: if there is 3 lines connecting to the same elements then it would be triple bond/3)\n")
if bond == "1":
    bondNum = "ane"
elif bond == "2":
    bondNum = "ene"
elif bond == "3":
    bondNum = "yne"

print(carbonNum + bondNum)
