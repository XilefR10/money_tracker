import functions

money = 1000
spent = []

while True:
    action = input("What do you want to do? (add/total/cat_total/average/cat_average/highest_spent/exit)\n>>")
    if action == "add":
        functions.add(spent)
    elif action == "total":
        functions.total_money(spent, money)
    elif action == "cat_total":
        functions.cat_total_money(spent)
    elif action == "exit":
        break
    elif action == "average":
        functions.average(spent)
    elif action == "cat_average":
        functions.cat_average(spent)
    elif action == "highest_spent":
        functions.highest_spent(spent)
    else:
        print("Invalid action. Please choose add, total, cat_total, average, cat_average, highest_spent, or exit.")