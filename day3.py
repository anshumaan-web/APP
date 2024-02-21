1. Method 1
def days_to_years_months_days(days):
    MONTH_DAYS = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31,
    }
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    days_remaining = remaining_days % 30
    return years, months, days_remaining
if __name__ == "__main__":
    total_days = int(input("Enter the total number of days: "))
    years, months, days_remaining = days_to_years_months_days(total_days)
    print(f"{total_days} days are equivalent to:")
    print(f"Years: {years}")
    print(f"Months: {months}")
    print(f"Days: {days_remaining}")



#2. Method 2
d = int(input("Enter the number of days: "))
year = d//365
print("No of years ",year)
remaining = d%365
month = remaining//30
print("No of months = ",month)
rem = remaining%30
print("No of remaining days are: ",rem)





import timeit
from memory_profiler import profile

@profile
def process_data(data):
    #Stimulate some processing on the data
    processed_data = [item.upper() for item in data]
    return processed_data

@profile
def main():
    data = ['item' + str(i) for i in range(100)] #Creating the list with 1 million items

    # Measure execution time using timelit
    execution_time = timeit.timeit(lambda: process_data(data), number=1)
    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()    