# Railway Reservation Analyzer (PS 76)
# This program reads bookings.csv and shows bookings per train
# and revenue per train (only confirmed tickets) with bar charts.

import os
import pandas as pd
import matplotlib.pyplot as plt


def read_file(filename):
    # check if file is there, if not show error and stop
    if not os.path.exists(filename):
        print("Error: File '" + filename + "' not found.")
        return None

    # try to read the file, handle the problems of an empty or damaged file
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

    # the program needs these columns, so check that they are present
    needed = ["PNR", "Train", "Fare", "Status"]
    missing = [col for col in needed if col not in data.columns]
    if len(missing) > 0:
        print("Error: Missing column(s) in file: " + ", ".join(missing))
        return None

    # remove spaces around the text so that matching works properly
    data["Train"] = data["Train"].str.strip()
    data["Status"] = data["Status"].str.strip()

    # convert fare to number, wrong values like abc will become NaN
    data["Fare"] = pd.to_numeric(data["Fare"], errors="coerce")

    # rows where fare is NaN are invalid so we print a warning for them
    bad_rows = data[data["Fare"].isna()]
    for pnr in bad_rows["PNR"]:
        print("Warning: Row with PNR " + str(pnr) + " skipped - invalid fare.")

    # keep only the rows which have a proper fare
    data = data.dropna(subset=["Fare"])

    print("Valid records analysed:", len(data))
    return data


def bookings_per_train(data):
    # group by train and count how many bookings each train has
    counts = data.groupby("Train").size()
    counts = counts.sort_values(ascending=False, kind="stable")

    for train in counts.index:
        print(train, ":", counts[train])
    print("Total bookings:", len(data))

    # bar chart for bookings
    plt.bar(counts.index, counts.values)
    plt.xlabel("Train")
    plt.ylabel("Number of bookings")
    plt.title("Bookings per Train")
    plt.show()


def revenue_per_train(data):
    # revenue is calculated only for confirmed tickets
    confirmed = data[data["Status"] == "Confirmed"]

    if len(confirmed) == 0:
        print("No confirmed tickets, revenue is Rs. 0")
        return

    revenue = confirmed.groupby("Train")["Fare"].sum()
    revenue = revenue.sort_values(ascending=False, kind="stable")

    for train in revenue.index:
        print(train, ": Rs.", int(revenue[train]))
    print("Total confirmed revenue: Rs.", int(revenue.sum()))

    # bar chart for revenue
    plt.bar(revenue.index, revenue.values)
    plt.xlabel("Train")
    plt.ylabel("Revenue (Rs.)")
    plt.title("Revenue per Train (Confirmed only)")
    plt.show()


def status_summary(data):
    # count of confirmed, waiting and cancelled tickets
    for status in ["Confirmed", "Waiting", "Cancelled"]:
        total = len(data[data["Status"] == status])
        print(status, ":", total)


def main():
    filename = input("Enter CSV file name (press Enter for bookings.csv): ").strip()
    if filename == "":
        filename = "bookings.csv"

    data = read_file(filename)
    if data is None:
        return

    # menu keeps repeating until user selects exit
    while True:
        print("\n--- Railway Reservation Analyzer ---")
        print("1. Bookings per train")
        print("2. Revenue per train")
        print("3. Status summary")
        print("4. Exit")
        choice = input("Enter your choice (number or name): ").strip().lower()

        # user can type the number or the name of the option
        if choice == "1" or choice == "bookings per train":
            bookings_per_train(data)
        elif choice == "2" or choice == "revenue per train":
            revenue_per_train(data)
        elif choice == "3" or choice == "status summary":
            status_summary(data)
        elif choice == "4" or choice == "exit":
            print("Thank you!")
            break
        else:
            print("Invalid choice, please enter 1 to 4 or the menu name.")


main()
