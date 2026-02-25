# Python Homework Template

A clean and well-configured Python project template for homework assignments. This template includes automatic code formatting, linting, and a virtual environment setup.

## Features

- 🎨 **Black** code formatter (auto-format on save)
- 🔍 **Pylint** for code quality checks
- 📦 Virtual environment support
- ⚙️ Pre-configured VS Code settings
- 📝 Clean project structure

## Initial Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.venv/Scripts/activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Working on Assignments

1. Open this project in VS Code
2. Ensure your virtual environment is activated
3. Create task files for your homework:
   - `task_1.py`
   - `task_2.py`
   - `task_3.py`
   - etc.

### Auto-Formatting

Code formatting is configured to run automatically on save:
- Uses **Black** formatter
- Max line length: 88 characters
- Tab size: 4 spaces

Simply write your code and save the file - it will be formatted automatically!

### Code Quality

Pylint is configured to check your code quality. VS Code will show warnings and suggestions as you code.

## Project Structure

```
simple-py-hw-template/
├── .venv/              # Virtual environment (not tracked in git)
├── .vscode/
│   └── settings.json   # VS Code configuration
├── .gitignore          # Git ignore rules
├── .pylintrc           # Pylint configuration
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── task_*.py          # Your homework files
```

## Notes

- The `.venv/` directory is included in `.gitignore` and will not be committed to git
- Always activate your virtual environment before working on assignments
- All dependencies are installed locally in the virtual environment

## Tips

- Run `pip list` to see installed packages
- Run `black .` to manually format all Python files
- Run `pylint task_1.py` to manually check a specific file

---

Happy coding! 🚀