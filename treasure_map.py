row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


first_number = int(position[0])
second_number = int(position[1])

if second_number == 1:
    row1[first_number - 1] = "X"
elif second_number == 2:
    row2[first_number - 1] = "X"
elif second_number == 3:
    row3[first_number - 1] = "X"
else:
    print("that is not a proper selection")

# ######## A Shorter Way####################
selected_row = map[second_number - 1]
selected_row[first_number - 1] = "X"
############################################

##############Or#############################
map[second_number - 1][first_number -1] = "X"
############################################

print(f"{row1}\n{row2}\n{row3}")