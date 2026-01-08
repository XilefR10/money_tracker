# Contributing to Money Tracker

Thank you for your interest in contributing to Money Tracker! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Be open to feedback and suggestions
- Help others learn and grow

## How to Contribute

### Reporting Bugs

1. **Check existing issues** - Search to see if the bug is already reported
2. **Create a new issue** with:
   - Clear title describing the bug
   - Detailed description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and OS
   - Any error messages or screenshots

### Suggesting Enhancements

1. **Use the Issues tab** to suggest new features
2. **Describe the feature** with:
   - What problem it solves
   - How users would benefit
   - Possible implementation approaches

### Making Code Changes

#### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/money_tracker.git
cd money_tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# For development/building
pip install pyinstaller
```

#### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow PEP 8 style guidelines
   - Add docstrings to functions
   - Write meaningful commit messages
   - Keep changes focused and atomic

3. **Test your changes**
   ```bash
   # Test the application
   python run.py
   
   # Or build executable
   python build_exe.py
   ```

4. **Commit your changes**
   ```bash
   git commit -m "Add: Description of your changes"
   ```

#### Commit Message Guidelines

- Start with a type: `Add:`, `Fix:`, `Refactor:`, `Docs:`, `Style:`
- Keep first line under 50 characters
- Provide detailed description in body
- Reference related issues with `#issue_number`

Examples:
```
Add: New export to CSV feature

Allows users to export transactions to CSV format
for use in spreadsheet applications.
Closes #123
```

```
Fix: Category average calculation error

The category average was counting wrong entries.
Updated filter logic to check exact category match.
```

#### Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Reference to related issues
- Any breaking changes noted
- Testing notes

## Code Style

### Python Style Guide (PEP 8)

```python
# Good
def calculate_total_spent(spent):
    """Calculate total amount spent."""
    return sum(entry["amount"] for entry in spent)

# Bad
def calc_tot(s):
    total=0
    for x in s: total+=x["amount"]
    return total
```

### Naming Conventions

- **Variables/Functions**: `lowercase_with_underscores`
- **Classes**: `PascalCase`
- **Constants**: `UPPERCASE_WITH_UNDERSCORES`
- **Private methods**: `_leading_underscore`

### Documentation

- Write docstrings for all functions
- Use triple quotes: `"""`
- Include parameter and return descriptions
- Add examples for complex functions

```python
def get_entries_by_category(spent, category):
    """Return all entries for a specific category.
    
    Args:
        spent (list): List of transaction dictionaries
        category (str): Category name to filter by
        
    Returns:
        list: Filtered list of entries
        
    Example:
        >>> entries = get_entries_by_category(data, "Food")
        >>> len(entries)
        5
    """
    return [entry for entry in spent if entry.get("category") == category]
```

## Project Structure

```
src/
  ├── main.py          # GUI application (tkinter)
  ├── functions.py     # Business logic
  └── __init__.py      # Package init

Tests should go in:
tests/
  ├── test_functions.py
  └── test_main.py
```

## Testing

While the project currently doesn't have automated tests, please:
- Manually test your changes thoroughly
- Test edge cases (empty data, large numbers, special characters)
- Test on Windows, macOS, and Linux if possible
- Test the GUI elements work as expected

## Building Releases

To build a release executable:

```bash
python build_exe.py
```

The executable will be in `dist/MoneyTracker.exe`.

## Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add comments for complex logic
- Keep documentation in sync with code

## Performance Considerations

- Handle large transaction lists efficiently
- Avoid unnecessary data processing
- Consider memory usage for charts
- Test with 1000+ transactions

## Security Considerations

- Validate user input
- Sanitize file paths
- Handle file I/O errors gracefully
- Don't store sensitive data in plain text

## Questions?

- Check existing issues and discussions
- Review the README and code documentation
- Ask in the issue tracker before starting major work

## Recognition

Contributors will be:
- Listed in the CONTRIBUTORS file
- Credited in releases
- Thanked in commit messages

---

Thank you for contributing! 🎉
