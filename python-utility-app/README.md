# Python Utility App

This project reads a CSV file, filters data based on a condition, and writes the result to a new file.

## 🛠 Requirements

- Python 3.10+
- No external packages required

## ▶️ Usage

```bash
python main.py --input data.csv --output result.csv
```

Only rows where the `active` column equals `yes` will be included in the output.

## 📄 Example CSV

```csv
id,name,active
1,Alice,yes
2,Bob,no
3,Charlie,yes
```

Output:

```csv
id,name,active
1,Alice,yes
3,Charlie,yes
```

## 📂 Structure

- `main.py`: Entry point with CLI
- `file_handler.py`: File reading/writing
- `processor.py`: Data processing logic
