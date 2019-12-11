
list = ""
num_of_errands = 1
hint_value = 3
print("\nWelcome to your To-Do List!\n\nPlease enter your errands one-by-one."
      "\nType \"done\" when complete.\n")

answer = input("What do you want to do? ").capitalize()

while answer != "done":
    if num_of_errands != hint_value:
        list += answer
        answer = input("Anything else? ")
        num_of_errands += 1
        if answer != "done":
            list += ", "
        else:
            list += "."
    else:
        hint_value += hint_value
        list += answer
        answer = input("Anything else? (Remember you can type \"done\" when complete.) ")
        num_of_errands += 1
        if answer != "done":
            list += ", "
        else:
            list += "."

if num_of_errands == 1:
    print("You have nothing to do today! Enjoy your freedom!")
elif num_of_errands == 2:
    print("\nYou have " + str(num_of_errands - 1) + " task to do.\nAll you have to do is: "
           + str(list))
else:
    print("\nYou have " + str(num_of_errands - 1) + " tasks to do.\nHere is your To-Do List for today: "
          + str(list) + "\n\nGood luck :)")
