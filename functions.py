import json
import os

# ===== DATA MANAGEMENT FUNCTIONS =====

def load_data():
    """Load data from JSON file. Returns default data if file doesn't exist."""
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {"money": 1000, "spent": []}

def save_data(money, spent):
    """Save money and spent list to JSON file."""
    data = {"money": money, "spent": spent}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

# ===== ENTRY MANAGEMENT FUNCTIONS =====

def add(spent):
    """Add a new spending or income entry to the list. Returns the amount and type."""
    new_entry = {}
    
    # Ask whether this is spending or income
    entry_type = input("Is this spending or income? (spending/income)\n>>").lower()
    if entry_type not in ["spending", "income"]:
        print("Invalid type. Please choose 'spending' or 'income'.")
        return 0, None
    
    new_entry["type"] = entry_type
    
    amount = int(input("How much?\n>>"))
    new_entry["amount"] = amount
    category = input("What category?\n>>")
    new_entry["category"] = category
    text = input("Add a name\n>>")
    new_entry["text"] = text
    spent.append(new_entry)
    print(spent)
    return amount, entry_type

# ===== VIEW FUNCTIONS =====

def total_money(spent, money):
    """Display total earned, total spent, and remaining balance."""
    money_spent = 0
    money_earned = 0
    
    # Separate spending and income entries
    for entry in spent:
        if entry["type"] == "spending":
            money_spent += entry["amount"]
        elif entry["type"] == "income":
            money_earned += entry["amount"]
    
    print("You have earned:", money_earned)
    print("You have spent:", money_spent)
    print("You have left:", money)

def cat_total_money(spent):
    """Display total spending for a specific category."""
    cat_money = 0
    category = input("For which category are you looking?\n>>")

    for i in spent:
        if category == i["category"]:
            cat_money += i["amount"]
            print(i) 
    print(cat_money)

def highest_spent(spent):
    """Display the spending entry with the highest amount."""
    # Filter only spending entries
    spending_entries = [entry for entry in spent if entry.get("type") == "spending"]
    
    if not spending_entries:
        print("No spending entries available.")
        return

    highest_entry = max(spending_entries, key=lambda x: x["amount"])

    print("The highest spending entry is:", highest_entry)

def highest_income(spent):
    """Display the income entry with the highest amount."""
    # Filter only income entries
    income_entries = [entry for entry in spent if entry.get("type") == "income"]
    
    if not income_entries:
        print("No income entries available.")
        return

    highest_entry = max(income_entries, key=lambda x: x["amount"])

    print("The highest income entry is:", highest_entry)

# ===== ANALYSIS FUNCTIONS =====

def average(spent):
    """Calculate and display average spending across all entries (spendings only)."""
    total = 0
    count = 0
    for i in spent:
        if i.get("type") == "spending":
            total += i["amount"]
            count += 1
    average_spent = total / count if count > 0 else 0
    print("Your average spending is:", average_spent)

def average_income(spent):
    """Calculate and display average income across income entries."""
    total = 0
    count = 0
    for i in spent:
        if i.get("type") == "income":
            total += i["amount"]
            count += 1
    average_inc = total / count if count > 0 else 0
    print("Your average income is:", average_inc)

def view_all_entries(spent):
    """Return and print a formatted report of all entries grouped by
    type (income/spending) and by category within each type.

    Returns the report string so callers (including a GUI) can display it.
    """
    if not spent:
        report = "No entries."
        print(report)
        return report

    grouped = {}
    for e in spent:
        t = e.get("type", "unknown")
        cat = e.get("category", "(uncategorized)")
        grouped.setdefault(t, {}).setdefault(cat, []).append(e)

    lines = []
    for t in ["income", "spending"]:
        lines.append(f"{t.title()} entries:")
        type_groups = grouped.get(t, {})
        if not type_groups:
            lines.append("  (none)")
            lines.append("")
            continue
        for cat, entries in type_groups.items():
            total = sum(x.get("amount", 0) for x in entries)
            lines.append(f"  Category: {cat}    Total: ${total}")
            for ent in entries:
                lines.append(f"    - {ent}")
        lines.append("")

    report = "\n".join(lines)
    print(report)
    return report

def cat_average(spent):
    """Calculate and display average spending for a specific category."""
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

# ===== MODIFICATION FUNCTIONS =====

def delete_entry(spent):
    """Delete a spending entry by index. Returns the refunded amount."""
    print("Current spending entries:")
    for index, entry in enumerate(spent):
        print(f"{index}: {entry}")
    index = int(input("Enter the index of the entry you want to delete:\n>>"))
    if 0 <= index < len(spent):
        deleted_entry = spent.pop(index)
        print("Deleted entry:", deleted_entry)
        return deleted_entry["amount"]
    else:
        print("Invalid index. Please try again.")
        return 0

def set_money(money):
    """Set/change the total money amount."""
    money = int(input("Set your total money amount:\n>>"))
    return money

def clear(spent):
    """Clear all entries and reset money to 1000."""
    spent.clear()
    return 1000