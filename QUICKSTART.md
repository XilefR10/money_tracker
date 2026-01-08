# Quick Start Guide

Get Money Tracker up and running in minutes!

## For Users

### Option 1: Use Pre-built Executable (Easiest)

1. **Download** `MoneyTracker.exe` from the `dist/` folder
2. **Run** it by double-clicking
3. **Done!** Start tracking your finances

⚠️ Keep `data.json` in the same folder as the .exe to save your data.

### Option 2: Run from Source Code

#### Prerequisites
- Python 3.8+ installed
- [Download Python](https://www.python.org/downloads/)

#### Steps

```bash
# 1. Clone or download the project
git clone https://github.com/yourusername/money_tracker.git
cd money_tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run.py
```

## For Developers

### Setup Development Environment

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/money_tracker.git
cd money_tracker

# 2. Create virtual environment (recommended)
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# For building executables
pip install pyinstaller
```

### Running the App

```bash
python run.py
```

### Making Changes

1. Edit code in `src/` folder
2. Test by running `python run.py`
3. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines

### Building a Release

```bash
python build_exe.py
```

The executable will be created in `dist/MoneyTracker.exe`.

## Common Tasks

### View All Dependencies
```bash
pip list
```

### Update Requirements
```bash
pip freeze > requirements.txt
```

### Run Code Quality Check
```bash
python -m py_compile src/*.py
```

### Check Project Structure
```bash
# Windows
tree /F /A

# macOS/Linux
tree -I '__pycache__|*.pyc'
```

## Project Files at a Glance

- **`run.py`** - Run the app
- **`build_exe.py`** - Build Windows executable
- **`src/main.py`** - GUI code
- **`src/functions.py`** - Business logic
- **`requirements.txt`** - Dependencies
- **`data/data.json`** - Your financial data
- **`README.md`** - Full documentation

## File Locations

### Where does my data get saved?
- Running from source: `data/data.json`
- Running executable: Same folder as `.exe`

### Where are the source files?
- `src/main.py` - GUI application
- `src/functions.py` - Calculations and data handling

## Troubleshooting

### "ModuleNotFoundError: No module named 'matplotlib'"
```bash
pip install matplotlib numpy
```

### "python command not found"
- Make sure Python is installed and added to PATH
- Try `python3` instead of `python`
- On Windows, use `py` instead of `python`

### Application won't start
1. Check Python version: `python --version` (must be 3.8+)
2. Check dependencies: `pip install -r requirements.txt`
3. Try running from source: `python run.py`

### Lost my data
- Data is saved in `data.json`
- Check if file exists in the data folder
- Restore from backup if available

## Next Steps

1. **Read** [README.md](README.md) for full feature list
2. **Check** [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for code organization
3. **See** [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
4. **Review** [CHANGELOG.md](CHANGELOG.md) for version history

## Getting Help

- 📖 Read documentation in README.md
- 🐛 Report bugs on GitHub Issues
- 💬 Discuss ideas on GitHub Discussions
- 📧 Contact via GitHub

## Tips

💡 **Pro Tips:**
- Use categories consistently for better analysis
- Check the Timeline view to see spending patterns
- Export your data regularly for backup
- Use the highest spending feature to find areas to cut

---

**Ready to start?** Run `python run.py` and add your first transaction!
