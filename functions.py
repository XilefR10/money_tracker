def total_money(spent, money):
    money_spent = 0
    for i in spent:
        money_spent += i["amount"]
    money -= money_spent

    print("You have spent:", money_spent)
    print("You have left:", money)

def cat_total_money(spent):
    cat_money = 0
    category = input("For which category are you looking?\n>>")

    for i in spent:
        if category == i["category"]:
            cat_money += i["amount"]
            print(i) 
    print(cat_money)

def add(spent):
    new_entry = {}
    amount = int(input("How much did you spent?\n>>"))
    new_entry["amount"] = amount
    category = input("What category?\n>>")
    new_entry["category"] = category
    text = input("Add a name\n>>")
    new_entry["text"] = text
    spent.append(new_entry)
    print(spent)

def average(spent):
    money = 0
    count = 0
    for i in spent:
        money += i["amount"]
    average_spent = money / count if count > 0 else 0
    print("Your average spending is:", average_spent)

def cat_average(spent):
    category = input("For which category are you looking?\n>>")
    cat_money = 0
    count = 0

    for i in spent:
        if category == i["category"]:
            cat_money += i["amount"]
            count += 1

    if count > 0:
        average = cat_money / count
        print(f"The average spending in category '{category}' is: {average}")
    else:
        print(f"No entries found for category '{category}'")

def highest_spent(spent):
    if not spent:
        print("No spending entries available.")
        return

    highest_entry = max(spent, key=lambda x: x["amount"])

    print("The highest spending entry is:", highest_entry)