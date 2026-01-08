import json
import os

# ===== DATA MANAGEMENT =====

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

# ===== FILTERING FUNCTIONS =====

def get_spending_entries(spent):
    """Return all spending entries."""
    return [entry for entry in spent if entry.get("type") == "spending"]

def get_income_entries(spent):
    """Return all income entries."""
    return [entry for entry in spent if entry.get("type") == "income"]

def get_entries_by_category(spent, category):
    """Return all entries for a specific category."""
    return [entry for entry in spent if entry.get("category") == category]

# ===== CALCULATION FUNCTIONS =====

def calculate_total_spent(spent):
    """Calculate total amount spent (sum of all spending entries)."""
    return sum(entry["amount"] for entry in get_spending_entries(spent))

def calculate_total_earned(spent):
    """Calculate total amount earned (sum of all income entries)."""
    return sum(entry["amount"] for entry in get_income_entries(spent))

def calculate_category_total(spent, category):
    """Calculate total amount for a specific category."""
    return sum(entry["amount"] for entry in get_entries_by_category(spent, category))

def calculate_average_spending(spent):
    """Calculate average spending amount across all entries."""
    spending_entries = get_spending_entries(spent)
    if not spending_entries:
        return 0
    return sum(entry["amount"] for entry in spending_entries) / len(spending_entries)

def calculate_category_average(spent, category):
    """Calculate average amount for a specific category."""
    category_entries = get_entries_by_category(spent, category)
    if not category_entries:
        return 0
    return sum(entry["amount"] for entry in category_entries) / len(category_entries)

# ===== ANALYSIS FUNCTIONS =====

def get_highest_spending_entry(spent):
    """Return the spending entry with the highest amount, or None if no spending entries."""
    spending_entries = get_spending_entries(spent)
    return max(spending_entries, key=lambda x: x["amount"]) if spending_entries else None

def get_highest_income_entry(spent):
    """Return the income entry with the highest amount, or None if no income entries."""
    income_entries = get_income_entries(spent)
    return max(income_entries, key=lambda x: x["amount"]) if income_entries else None

def get_totals(spent, money):
    """Return a dict with total earned, total spent, and current balance."""
    return {
        "earned": calculate_total_earned(spent),
        "spent": calculate_total_spent(spent),
        "balance": money
    }

def get_chart_data(spent):
    """Return chart data: earned and spent amounts for visualization."""
    return {
        "earned": calculate_total_earned(spent),
        "spent": calculate_total_spent(spent)
    }

def get_timeline_data(spent, starting_money):
    """Calculate money balance at each point in the timeline.
    
    Returns a list of tuples: (money_amount, entry_label)
    """
    timeline = [(starting_money, "Start")]
    current_balance = starting_money
    
    for i, entry in enumerate(spent, 1):
        if entry["type"] == "spending":
            current_balance -= entry["amount"]
        else:  # income
            current_balance += entry["amount"]
        
        label = entry.get("text", f"Entry {i}")
        timeline.append((current_balance, label))
    
    return timeline

# ===== FORMATTING & DISPLAY FUNCTIONS =====

def format_all_entries(spent):
    """Return a formatted report of all entries grouped by type and category."""
    if not spent:
        return "No entries."

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

    return "\n".join(lines)

def format_entries_for_display(spent):
    """Return a formatted list of entries with indices for selection."""
    return "\n".join([f"{i}: {entry}" for i, entry in enumerate(spent)])

# ===== LEGACY FUNCTIONS (CLI ONLY) =====

def view_all_entries(spent):
    """Return and print a formatted report of all entries (for backward compatibility)."""
    report = format_all_entries(spent)
    print(report)
    return report

def total_money(spent, money):
    """Display total earned, total spent, and remaining balance (legacy CLI function)."""
    totals = get_totals(spent, money)
    print("You have earned:", totals["earned"])
    print("You have spent:", totals["spent"])
    print("You have left:", totals["balance"])

def cat_total_money(spent):
    """Display total spending for a specific category (legacy CLI function)."""
    category = input("For which category are you looking?\n>>")
    cat_money = calculate_category_total(spent, category)
    entries = get_entries_by_category(spent, category)
    for entry in entries:
        print(entry)
    print(cat_money)

def highest_spent(spent):
    """Display the spending entry with the highest amount (legacy CLI function)."""
    entry = get_highest_spending_entry(spent)
    if entry:
        print("The highest spending entry is:", entry)
    else:
        print("No spending entries available.")

def highest_income(spent):
    """Display the income entry with the highest amount (legacy CLI function)."""
    entry = get_highest_income_entry(spent)
    if entry:
        print("The highest income entry is:", entry)
    else:
        print("No income entries available.")

def average(spent):
    """Calculate and display average spending (legacy CLI function)."""
    avg = calculate_average_spending(spent)
    print("Your average spending is:", avg)

def average_income(spent):
    """Calculate and display average income (legacy CLI function)."""
    income_entries = get_income_entries(spent)
    if not income_entries:
        print("Your average income is: 0")
        return
    avg = sum(entry["amount"] for entry in income_entries) / len(income_entries)
    print("Your average income is:", avg)

def cat_average(spent):
    """Calculate and display average spending for a specific category (legacy CLI function)."""
    category = input("For which category are you looking?\n>>")
    avg = calculate_category_average(spent, category)
    if avg == 0 and not get_entries_by_category(spent, category):
        print(f"No entries found for category '{category}'")
    else:
        print(f"The average spending in category '{category}' is: {avg}")

def delete_entry(spent):
    """Delete a spending entry by index (legacy CLI function). Returns the refunded amount."""
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
    """Set/change the total money amount (legacy CLI function)."""
    money = int(input("Set your total money amount:\n>>"))
    return money

def clear(spent):
    """Clear all entries and reset money to 1000 (legacy CLI function)."""
    spent.clear()
    return 1000