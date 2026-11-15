# Project Summary: Railway Reservation Analyzer (PS No. 76)

## Objective

The aim of this project is to analyze railway booking data stored in a CSV file. The program reads the data using Pandas, shows the number of bookings and the revenue for each train, and displays the results as bar charts using Matplotlib.

## Technologies Used

Python 3, Pandas (data reading and grouping), Matplotlib (bar charts), and the `os` module (file checking).

## Approach

1. The program asks for the CSV file name. If nothing is entered, it uses `bookings.csv` by default.
2. It checks whether the file exists. If not, it shows an error message instead of crashing.
3. The data is read into a Pandas DataFrame, and extra spaces in the Train and Status columns are removed.
4. The Fare column is converted to numbers using `pd.to_numeric` with `errors="coerce"`. Invalid values such as "abc" become NaN, and those rows are skipped with a warning that shows the PNR.
5. The number of valid records analysed is displayed.
6. A menu lets the user choose an option by number or by name.

## Features

- **Bookings per train:** the data is grouped by train and the bookings are counted. The trains are shown in descending order along with the total bookings and a bar chart.
- **Revenue per train:** only tickets with Confirmed status are considered. The fares are grouped by train and summed. The program shows each train's revenue, the total confirmed revenue and a bar chart.
- **Status summary:** shows the count of Confirmed, Waiting and Cancelled tickets.

## Error Handling

- A missing file shows: `Error: File 'missing.csv' not found.`
- A row with an invalid fare is skipped with a warning: `Warning: Row with PNR 1011 skipped - invalid fare.`
- An invalid menu choice shows a message and the menu is displayed again.

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

![Test Case 1 output](<test case 1.png>)

**Bar chart**

![Test Case 1 graph](<test case 1 graph.png>)

### Test Case 2: Boundary / Minimum Input

Input: `one.csv` (only one data row), menu option "Revenue per train"

**Terminal output**

![Test Case 2 output](<test case 2.png>)

**Bar chart**

![Test Case 2 graph](<test case 2 graph.png>)

### Test Case 3: Invalid Input

**(a) Missing file:** `missing.csv`

![Test Case 3a output](<test case 3 (a).png>)

**(b) Invalid fare:** `extra.csv` (extra row `1011,Gondwana,SL,abc,Confirmed`)

![Test Case 3b output](<test case 3 (b).png>)

### Test Case 4: Different Valid Scenario

Input: `bookings.csv`, menu option "Revenue per train"

**Terminal output**

![Test Case 4 output](<test case 4.png>)

**Bar chart**

![Test Case 4 graph](<test case 4 graph.png>)

## Concepts Covered

Functions, loops, conditional statements, file handling, exception and error handling, CSV reading with Pandas, filtering, grouping (`groupby`), and data visualization with Matplotlib.

## Conclusion

The program meets all the requirements of the problem statement. It handles missing files and invalid data without crashing, and it gives clear train-wise results with charts for both bookings and revenue.