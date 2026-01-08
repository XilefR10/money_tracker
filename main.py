import functions

# Load data from JSON file
data = functions.load_data()
money = data["money"]
spent = data["spent"]

# Main application loop
while True:
    action = input("What do you want to do? (add/total/cat_total/highest_spent/highest_income/average/cat_average/delete_entry/set_money/clear/exit)\n>>")
    # Add a new spending or income entry
    if action == "add":
        amount, entry_type = functions.add(spent)
        if entry_type == "spending":
            money -= amount  # Decrease money when spending
        elif entry_type == "income":
            money += amount  # Increase money when adding income
        functions.save_data(money, spent)
    # Display total spending and remaining balance
    elif action == "total":
        functions.total_money(spent, money)
    # Display total spending for a specific category
    elif action == "cat_total":
        functions.cat_total_money(spent)
    # Display the highest spending entry
    elif action == "highest_spent":
        functions.highest_spent(spent)
    # Display the highest income entry
    elif action == "highest_income":
        functions.highest_income(spent)
    # Calculate average spending across all entries
    elif action == "average":
        functions.average(spent)
    # Calculate average spending for a specific category
    elif action == "cat_average":
        functions.cat_average(spent)
    # Delete a spending entry and refund the amount
    elif action == "delete_entry":
        amount = functions.delete_entry(spent)
        money += amount  # Increase money by the refunded amount
        functions.save_data(money, spent)
    # Exit the application
    elif action == "exit":
        break
    # Set/change the total money amount
    elif action == "set_money":
        money = functions.set_money(money)
        functions.save_data(money, spent)
    # Clear all entries and reset money to 1000
    elif action == "clear":
        money = functions.clear(spent)
        functions.save_data(money, spent)
    # Handle invalid actions
    else:
        print("Invalid action. Please choose add, total, cat_total, highest_spent, highest_income, average, cat_average, delete_entry, set_money, clear, or exit.")