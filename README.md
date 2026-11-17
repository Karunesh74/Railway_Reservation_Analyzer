# Railway Reservation Analyzer (PS 76)
## Student Details
- **Name:** Karunesh Baghwar
- **Class/Section:** SA16 section-M
- **ERP:** RU-26-00283


A Python program that reads railway booking data from a CSV file and shows how many bookings each train has and how much revenue each train earns. The results are also shown as bar charts.

## What the program does

- Reads `bookings.csv` using Pandas
- Shows the number of valid records analysed
- Skips rows that have an invalid fare and prints a warning for them
- Shows **bookings per train** with a bar chart
- Shows **revenue per train** (only Confirmed tickets) with a bar chart
- Shows a **status summary** (Confirmed, Waiting and Cancelled tickets)
- Shows an error message if the file is missing, instead of crashing

## Technologies used

- Python 3
- Pandas
- Matplotlib

## Project files

| File | Description |
|---|---|
| `railway.py` | Main program |
| `bookings.csv` | Sample data (10 rows) |
| `one.csv` | Test file with only one data row (Test Case 2) |
| `extra.csv` | Sample data plus one row with an invalid fare (Test Case 3b) |
| `summary.md` | Project summary |
| `test case ... .png` | Screenshots of the test case outputs |

## Input file format

The CSV file must have these 5 columns:

```
PNR,Train,Class,Fare,Status
1001,Shatabdi,CC,950,Confirmed
1002,Shatabdi,CC,950,Confirmed
1003,Shatabdi,EC,1800,Waiting
```

`Status` can be Confirmed, Waiting or Cancelled.

## How to run

1. Install Python 3 from python.org
2. Install the required libraries:
   ```
   pip install pandas matplotlib
   ```
3. Keep `railway.py` and `bookings.csv` in the same folder
4. Run the program:
   ```
   python railway.py
   ```
   On Windows you can also use `py railway.py`.
5. When it asks for the file name, press Enter to use `bookings.csv`, or type another file name.
6. Choose an option from the menu. You can type the number or the name of the option.

## Menu

```
1. Bookings per train
2. Revenue per train
3. Status summary
4. Exit
```

After a bar chart opens, close the chart window to come back to the menu.

## Sample output

**Bookings per train**

```
Gondwana : 4
Rajdhani : 3
Shatabdi : 3
Total bookings: 10
```

**Revenue per train (Confirmed tickets only)**

```
Rajdhani : Rs. 4100
Gondwana : Rs. 2540
Shatabdi : Rs. 1900
Total confirmed revenue: Rs. 8540
```

## Test cases

| Test case | Input | Expected result |
|---|---|---|
| 1. Normal input | `bookings.csv`, Bookings per train | Gondwana 4, Rajdhani 3, Shatabdi 3, total 10, bar chart with 3 bars |
| 2. Minimum input | `one.csv`, Revenue per train | Shatabdi Rs. 950, total Rs. 950, bar chart with 1 bar |
| 3a. Missing file | `missing.csv` | `Error: File 'missing.csv' not found.` |
| 3b. Invalid fare | `extra.csv` | `Warning: Row with PNR 1011 skipped - invalid fare.` and `Valid records analysed: 10` |
| 4. Different valid scenario | `bookings.csv`, Revenue per train | Rajdhani Rs. 4100, Gondwana Rs. 2540, Shatabdi Rs. 1900, total Rs. 8540 |

## Concepts used

Functions, loops, conditional statements, file handling, error handling, Pandas (CSV reading, filtering, `groupby`), and Matplotlib bar charts.
