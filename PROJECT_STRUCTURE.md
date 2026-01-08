# Project Structure

This document explains the organization of the Money Tracker project.

## Directory Layout

```
money_tracker/
├── src/                          # Source code package
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # GUI application (tkinter)
│   └── functions.py             # Business logic & calculations
│
├── data/                         # User data storage
│   ├── .gitkeep                 # Placeholder for git tracking
│   └── data.json                # User financial data (generated)
│
├── dist/                         # Distribution (generated)
│   └── MoneyTracker.exe         # Standalone Windows executable
│
├── build/                        # Build artifacts (generated, ignored)
│
├── run.py                        # Entry point for development
├── build_exe.py                  # Executable builder script
├── setup.py                      # Python package setup
│
├── README.md                     # Main documentation
├── CONTRIBUTING.md               # Contribution guidelines
├── CHANGELOG.md                  # Version history
├── PROJECT_STRUCTURE.md          # This file
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
└── requirements.txt              # Python dependencies
```

## Key Files

### Source Code (src/)

| File | Purpose | Key Classes/Functions |
|------|---------|---------------------|
| `__init__.py` | Package initialization | Version info, imports |
| `main.py` | GUI application | `MoneyTrackerApp`, `run()` |
| `functions.py` | Business logic | Calculations, data handling |

### Root Directory

| File | Purpose |
|------|---------|
| `run.py` | Development entry point |
| `build_exe.py` | Build standalone executable |
| `setup.py` | Python package configuration |
| `requirements.txt` | Dependencies list |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | User guide & overview |
| `CONTRIBUTING.md` | Developer guidelines |
| `CHANGELOG.md` | Version history |
| `LICENSE` | MIT License |
| `PROJECT_STRUCTURE.md` | This file |

## Data Flow

```
User Input (GUI)
    ↓
main.py (UI Logic)
    ↓
functions.py (Business Logic)
    ↓
data/data.json (Persistent Storage)
```

## Code Organization

### src/main.py
- `MoneyTrackerApp` class - Main GUI application
- `_create_button()` - Button styling helper
- `_modal_add_entry()` - Entry dialog
- `_modal_single_input()` - Input dialog
- Action methods: `add_entry()`, `view_total()`, etc.

### src/functions.py
- **Data Management**: `load_data()`, `save_data()`
- **Filtering**: `get_spending_entries()`, `get_income_entries()`, etc.
- **Calculations**: `calculate_*()` functions
- **Analysis**: `get_highest_*()`, `get_chart_data()`, etc.
- **Formatting**: `format_all_entries()`, `format_entries_for_display()`
- **Legacy**: CLI-only functions for backward compatibility

## Build Artifacts (Ignored)

These folders are auto-generated and not committed:
- `build/` - PyInstaller build intermediate files
- `dist/` - Built executable (except repo might include binary for releases)
- `__pycache__/` - Python bytecode cache
- `*.spec` - PyInstaller configuration
- `.venv/` - Virtual environment

## Data Storage

### data/data.json Format
```json
{
  "money": 1500.00,
  "spent": [
    {
      "type": "spending",
      "amount": 50.00,
      "category": "Food",
      "text": "Groceries"
    }
  ]
}
```

## Dependencies

### Runtime
- tkinter (built-in with Python)
- matplotlib >= 3.8.0
- numpy >= 1.24.0

### Development/Build
- PyInstaller (for executable)
- setuptools (for packaging)

## Working with This Structure

### Development
```bash
python run.py
```

### Building Executable
```bash
python build_exe.py
```

### Installing as Package
```bash
pip install -e .
```

### Running Tests
```bash
pytest tests/
```

## Module Dependencies

```
src/main.py imports:
  - tkinter (stdlib)
  - matplotlib (external)
  - src.functions (local)

src/functions.py imports:
  - json (stdlib)
  - os (stdlib)

run.py imports:
  - src.main
```

## File Sizes Reference

Typical file sizes:
- `src/main.py` - ~18 KB (GUI code)
- `src/functions.py` - ~8 KB (Business logic)
- `MoneyTracker.exe` - ~36 MB (Standalone executable)
- `data.json` - Few KB (User data)

## Adding New Features

### Adding a new analysis function:
1. Create function in `src/functions.py`
2. Add UI button in `src/main.py`
3. Call function from button handler

### Adding a new chart type:
1. Create calculation in `src/functions.py`
2. Create chart window in `src/main.py`
3. Use matplotlib for visualization

## Version Control

### What's Committed
- Source code (`src/`)
- Documentation (`.md` files)
- Configuration (`requirements.txt`, `setup.py`)
- License and guidelines

### What's Ignored
- Build artifacts (`build/`, `dist/`)
- Cache files (`__pycache__/`)
- Virtual environments (`.venv/`)
- User data (`data.json`)
- IDE files (`.vscode/`, `.idea/`)

## Contributing

When contributing, maintain this structure:
- Code changes → `src/` folder
- Documentation updates → root directory
- New features → add to appropriate module
- Data access → through `src/functions.py`

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

Last Updated: January 2026
