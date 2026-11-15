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

Functions, loops, conditional statements, file handling, exception and error handling, CSV reading with Pandas, filtering, grouping (`groupby`), and data visualization with Matplotlib.

## Conclusion

The program meets all the requirements of the problem statement. It handles missing files and invalid data without crashing, and it gives clear train-wise results with charts for both bookings and revenue.
