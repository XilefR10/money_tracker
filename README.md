# Money Tracker

A simple command-line application to track and analyze your spending.

## Features

- **Add Spending**: Record new spending entries with amount, category, and description
- **Total Spending**: View total amount spent and remaining balance
- **Category Totals**: Calculate total spending for a specific category
- **Average Spending**: Calculate the average amount spent across all entries
- **Category Average**: Calculate the average spending for a specific category
- **Highest Spent**: Find the entry with the highest spending amount

## How to Use

1. Run the application:
   ```
   python main.py
   ```

2. Choose an action from the menu:
   - `add` - Add a new spending entry
   - `total` - View total spending and remaining balance
   - `cat_total` - View total spending for a category
   - `average` - Calculate average spending across all entries
   - `cat_average` - Calculate average spending for a category
   - `highest_spent` - Find the highest spending entry
   - `exit` - Exit the application

## Getting Started

When you run the program, you start with a balance of $1000. Follow the prompts to add spending entries and analyze your spending habits.

### Example Usage

```
What do you want to do? (add/total/cat_total/average/cat_average/highest_spent/exit)
>> add
How much did you spent?
>> 50
What category?
>> Food
Add a name
>> Groceries
```

## Requirements

- Python 3.x

## Files

- `main.py` - Main application loop
- `functions.py` - Core functionality for all features
- `README.md` - This file