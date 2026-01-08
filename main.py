import functions

# Load data from JSON file
data = functions.load_data()
money = data["money"]
spent = data["spent"]

# Main application loop
while True:
    action = input("What do you want to do? (add/total/cat_total/highest_spent/average/cat_average/delete_entry/set_money/exit)\n>>")
    # Add a new spending entry
    if action == "add":
        amount = functions.add(spent)
        money -= amount  # Decrease money by the amount spent
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
    # Handle invalid actions
    else:
        print("Invalid action. Please choose add, total, cat_total, highest_spent, average, cat_average, delete_entry, set_money, or exit.")