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
# Money Tracker

A small GUI application to track incomes and spendings, analyze totals, and visualize data.

**Features**
- Add Entry (spending or income) with amount, category, description
- View Total (earned, spent, remaining)
- View Chart (bar + pie chart for income vs spending)
- View All (grouped by type and by category)
- Category Total & Category Average
- Highest Spending / Highest Income
- Average Spending (spendings only) and Average Income
- Delete Entry, Set Money, Clear All

**Install**
1. (Optional) create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Upgrade packaging tools and install dependencies (uses binary wheels where possible):
   ```powershell
   python -m pip install --upgrade pip setuptools wheel
   pip install --only-binary=:all: -r requirements.txt
   ```
3. If installation fails while building packages (numpy/matplotlib), either re-run the command with `--only-binary` or install the Visual C++ Build Tools from Microsoft.

Note: `tkinter` is included with standard CPython on Windows; no extra install is required for it.

**Run**
```powershell
python main.py
```

The app opens a window. Use the buttons to add entries, view summaries, charts, and the full report.

**Files**
- [main.py](main.py) — GUI application
- [functions.py](functions.py) — core data operations
- [requirements.txt](requirements.txt) — external dependencies (matplotlib, numpy)
- [data.json](data.json) — persistent data file created/updated by the app

If you'd like, I can add screenshots to this README or wire the `view_all` output into a printable/exportable text file.