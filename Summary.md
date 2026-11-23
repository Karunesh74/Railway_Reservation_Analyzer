# Project Summary: Railway Reservation Analyzer (PS No. 76)

## Objective

The aim of this project is to analyze railway booking data stored in a CSV file. The program reads the data using Pandas, shows the number of bookings and the revenue for each train, and displays the results as bar charts using Matplotlib.

## Technologies Used

Python 3, Pandas (data reading and grouping), Matplotlib (bar charts), and the `os` module (file checking).

## Approach

1. The program asks for the CSV file name. If nothing is entered, it uses `bookings.csv` by default.
2. It checks whether the file exists. If not, it shows an error message instead of crashing.
3. The file is read into a Pandas DataFrame inside a `try/except` block. An empty or damaged file shows an error message. The required columns are also checked.
4. Extra spaces in the Train and Status columns are removed.
5. The Fare column is converted to numbers using `pd.to_numeric` with `errors="coerce"`. Invalid values such as "abc" become NaN, and those rows are skipped with a warning that shows the PNR.
6. The number of valid records analysed is displayed.
7. A menu lets the user choose an option by number or by name.

## Features

- **Bookings per train:** the data is grouped by train and the bookings are counted. The trains are shown in descending order along with the total bookings and a bar chart.
- **Revenue per train:** only tickets with Confirmed status are considered. The fares are grouped by train and summed. The program shows each train's revenue, the total confirmed revenue and a bar chart.
- **Status summary:** shows the count of Confirmed, Waiting and Cancelled tickets.

## Error Handling (with the exact lines of code)

The program handles errors in `read_file()`, `revenue_per_train()` and `main()`. Each problem is explained below with the line of code that handles it.

### 1. Missing file

```python
if not os.path.exists(filename):
    print("Error: File '" + filename + "' not found.")
    return None
```

- `os.path.exists(filename)` checks whether the file is present in the folder.
- If it is not present, a clear message is printed: `Error: File 'missing.csv' not found.`
- `return None` stops `read_file()` and sends `None` back, which means "no data".
- In `main()`, the lines `if data is None: return` end the program safely, so the menu is never shown without data.

### 2. Empty, damaged or unreadable file

```python
try:
    data = pd.read_csv(filename)
except pd.errors.EmptyDataError:
    print("Error: File '" + filename + "' is empty.")
    return None
except (pd.errors.ParserError, UnicodeDecodeError):
    print("Error: File '" + filename + "' is not a proper CSV file.")
    return None
except OSError:
    print("Error: File '" + filename + "' could not be opened.")
    return None
```

- `try:` runs the risky line `pd.read_csv(filename)`. If an error happens, Python jumps to the matching `except` block instead of stopping the program.
- `pd.errors.EmptyDataError` is raised when the file has no data. The program prints "is empty" and returns `None`.
- `pd.errors.ParserError` and `UnicodeDecodeError` are raised when the file is not a proper text CSV file (for example, an Excel or image file). The program prints "is not a proper CSV file".
- `OSError` covers other problems such as a folder name given as the file name or no permission to open the file. It is written last because the other errors are special cases of it.

### 3. Required column missing

```python
needed = ["PNR", "Train", "Fare", "Status"]
missing = [col for col in needed if col not in data.columns]
if len(missing) > 0:
    print("Error: Missing column(s) in file: " + ", ".join(missing))
    return None
```

- `needed` lists the columns the program uses.
- The second line builds a list of the columns that are not present in the file.
- If the list is not empty, the program prints which column is missing (for example `Fare`) and returns `None`. Without this check, the next lines would crash with a `KeyError`.

### 4. Invalid or blank fare

```python
data["Fare"] = pd.to_numeric(data["Fare"], errors="coerce")
bad_rows = data[data["Fare"].isna()]
for pnr in bad_rows["PNR"]:
    print("Warning: Row with PNR " + str(pnr) + " skipped - invalid fare.")
data = data.dropna(subset=["Fare"])
```

- `pd.to_numeric(..., errors="coerce")` converts Fare to numbers. A wrong value such as `abc` does not cause an error; it becomes NaN.
- `data["Fare"].isna()` finds the rows whose fare is NaN, and `bad_rows` holds those rows.
- The `for` loop prints a warning with the PNR of every bad row. `str(pnr)` is used because the PNR is a number and must be joined with text.
- `dropna(subset=["Fare"])` removes those rows, so the rest of the data is analysed normally.

### 5. No Confirmed tickets

```python
confirmed = data[data["Status"] == "Confirmed"]
if len(confirmed) == 0:
    print("No confirmed tickets, revenue is Rs. 0")
    return
```

- The first line keeps only the Confirmed tickets.
- If there are none, a message is printed and the function returns. This avoids an empty chart or an error.

### 6. Wrong menu choice

```python
else:
    print("Invalid choice, please enter 1 to 4 or the menu name.")
```

- This `else` runs when the user types anything that is not 1 to 4 or an option name. The message is printed and the `while True` loop shows the menu again.

## Results on Sample Data

| Train | Bookings | Confirmed Revenue |
|---|---|---|
| Gondwana | 4 | Rs. 2540 |
| Rajdhani | 3 | Rs. 4100 |
| Shatabdi | 3 | Rs. 1900 |
| **Total** | **10** | **Rs. 8540** |

All four test cases (normal input, single-row input, invalid input and a different valid scenario) give the expected output.

## Test Case Screenshots

### Test Case 1: Normal Input

Input: `bookings.csv`, menu option "Bookings per train"

**Terminal output**

<img width="1412" height="728" alt="test case 1" src="https://github.com/user-attachments/assets/857b51c7-e9bb-418c-b013-5da0c36cc5f0" />


**Bar chart**

<img width="640" height="480" alt="test case 1 graph" src="https://github.com/user-attachments/assets/c2ffe6bd-833c-4459-962f-931d52716d02" />


### Test Case 2: Boundary / Minimum Input

Input: `one.csv` (only one data row), menu option "Revenue per train"

**Terminal output**

<img width="1451" height="681" alt="test case 2" src="https://github.com/user-attachments/assets/6b6ffa30-760c-482f-85e7-ea43f2169053" />


**Bar chart**

<img width="640" height="480" alt="test case 2 graph" src="https://github.com/user-attachments/assets/5e9c8a93-82dd-4607-a3a5-cbdb2d1e9e34" />


### Test Case 3: Invalid Input

**(a) Missing file:** `missing.csv`

<img width="1512" height="201" alt="test case 3 (a)" src="https://github.com/user-attachments/assets/48759b62-bc28-4859-bd01-3ebd59ba84b2" />


**(b) Invalid fare:** `extra.csv` (extra row `1011,Gondwana,SL,abc,Confirmed`)

<img width="1507" height="133" alt="test case 3 (b)" src="https://github.com/user-attachments/assets/427fc989-4b63-4aff-bdf6-b2fba03d741d" />


### Test Case 4: Different Valid Scenario

Input: `bookings.csv`, menu option "Revenue per train"

**Terminal output**

<img width="1523" height="378" alt="test case 4" src="https://github.com/user-attachments/assets/35667b30-bb57-4237-877b-a47a40cb72e1" />


**Bar chart**

<img width="640" height="480" alt="test case 4 graph" src="https://github.com/user-attachments/assets/628c5ef9-c3a9-4cad-b970-dccd64efbdf0" />


## Concepts Covered

Functions, loops, conditional statements, file handling, exception and error handling (`os.path.exists`, `try/except`), CSV reading with Pandas, filtering, grouping (`groupby`), and data visualization with Matplotlib.

## Conclusion

The program meets all the requirements of the problem statement. It handles missing, empty and damaged files and invalid data without crashing, and it gives clear train-wise results with charts for both bookings and revenue.
