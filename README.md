# 💰 Money Tracker

A modern, user-friendly GUI application for personal finance management. Track your income and expenses with ease, visualize your spending patterns, and analyze your financial habits.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Building Executable](#building-executable)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality
- ✅ **Add Entries** - Record income and spending with category and description
- ✅ **View Totals** - See total earned, spent, and current balance at a glance
- ✅ **Financial Charts** - Visualize your data with bar charts and pie charts
- ✅ **Timeline View** - Track your money balance over time with a line graph
- ✅ **Category Analysis** - View spending by category with totals and averages
- ✅ **Statistics** - Find highest spending, highest income, and calculate averages

### User Experience
- 🎨 **Modern UI** - Beautiful, organized interface with color-coded sections
- 📊 **Multiple Visualizations** - Charts, timelines, and detailed reports
- 💾 **Data Persistence** - Automatically saves your data to JSON
- 🖱️ **Intuitive Controls** - Easy-to-use buttons and modal dialogs
- 🔒 **Safe Operations** - Confirmation dialogs for destructive actions

## 📸 Screenshots

The application features:
- **Dashboard Header** - Prominent balance display
- **Quick Actions** - Frequently used operations in blue
- **Analytics Section** - Timeline, view all, category analysis in purple
- **Statistics Section** - Highest spending/income, averages in red
- **Settings & Management** - Category operations, delete, set balance in green
- **Danger Zone** - Clear all data and exit in orange/red

## 🚀 Installation

### Option 1: Run from Source (Recommended for Development)

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

#### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/money_tracker.git
   cd money_tracker
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

### Option 2: Use Pre-built Executable (Windows)

1. **Download** the latest `MoneyTracker.exe` from the dist folder
2. **Run** the executable by double-clicking it
3. **Place** `data.json` in the same folder to save your data

## 📖 Usage

### Starting the Application

```bash
python run.py
```

### Main Features

#### Adding Entries
1. Click **"➕ Add Entry"**
2. Select type: Spending or Income
3. Enter amount, category, and description
4. Click OK

#### Viewing Data
- **View Total** - Summary of earned, spent, and remaining
- **View Chart** - Bar and pie charts
- **View All** - Complete list of all entries
- **Timeline** - Track balance changes over time

#### Analytics
- **Category Total** - Sum of all transactions in a category
- **Highest Spending** - Your largest expense
- **Highest Income** - Your largest income
- **Average Spending** - Mean of all transactions
- **Category Average** - Mean spending in a category

#### Management
- **Delete Entry** - Remove unwanted transactions
- **Set Balance** - Manually adjust your balance
- **Clear All** - Reset everything (with confirmation)

### Data Storage

Your data is automatically saved to `data.json` in the same directory:
- Location: `data/data.json` when running from source
- Location: Same folder as `MoneyTracker.exe` when using the executable

## 📁 Project Structure

```
money_tracker/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── main.py              # GUI application and UI logic
│   └── functions.py         # Business logic and calculations
├── data/                    # User data storage
│   └── .gitkeep
├── dist/                    # Built executables (generated)
├── build/                   # Build artifacts (generated)
├── run.py                   # Entry point for development
├── build_exe.py             # Executable builder script
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── .gitignore               # Git ignore rules
└── LICENSE                  # License file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `src/main.py` | GUI application with tkinter |
| `src/functions.py` | Business logic, calculations, data management |
| `src/__init__.py` | Package initialization |
| `run.py` | Entry point for running the application |
| `build_exe.py` | Script to build standalone Windows executable |
| `requirements.txt` | Python package dependencies |

## 🔧 Requirements

### Runtime Requirements
- Python 3.8+
- tkinter (usually included with Python)
- matplotlib >= 3.8.0
- numpy >= 1.24.0

### Development Requirements
- PyInstaller (for building executables)
- All runtime requirements

See `requirements.txt` for the complete list.

## 🛠️ Building Executable

To create a standalone `MoneyTracker.exe` for Windows:

```bash
# Install PyInstaller if not already installed
pip install pyinstaller

# Run the build script
python build_exe.py
```

The executable will be created in the `dist/` folder. It's completely self-contained and includes all dependencies.

### Build Features
- ✅ Automatically cleans old builds
- ✅ Creates single `.exe` file
- ✅ No installation required on target PC
- ✅ Works on Windows 10/11

## 📊 Data Format

The application uses JSON for data storage:

```json
{
  "money": 1500.00,
  "spent": [
    {
      "type": "spending",
      "amount": 50.00,
      "category": "Food",
      "text": "Groceries"
    },
    {
      "type": "income",
      "amount": 2000.00,
      "category": "Salary",
      "text": "Monthly salary"
    }
  ]
}
```

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Code Style
- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and testable

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI
- Uses [matplotlib](https://matplotlib.org/) for data visualization
- Packaged with [PyInstaller](https://pyinstaller.org/)

## 📧 Contact & Support

For issues, questions, or suggestions:
- Open an [issue](https://github.com/yourusername/money_tracker/issues)
- Check existing issues first
- Provide detailed information about your problem

---

**Made with ❤️ for personal finance management**
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