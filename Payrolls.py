import pandas as pd
import numpy as np
from fredapi import Fred
from Template import create_economic_chart
from APIkeys import FKEY

# Set up FRED API access
fred = Fred(api_key=FKEY)

def fetch_fred_data(series_id):
    """Fetches and returns the time series data from FRED."""
    data = fred.get_series(series_id)
    return data.index, data.values  # Return both the index (dates) and the values

def calculate_monthly_change(x, y):
    """Calculates the month-on-month change for a given time series."""
    monthly_change = [0]  # Start with 0 for the first month
    for i in range(1, len(y)):
        change = y[i] - y[i-1]
        monthly_change.append(change)
    return x, monthly_change

def calculate_moving_average(x, y, window):
    """Calculates moving average over a specified window."""
    moving_avg = y.rolling(window=window, min_periods=1).mean()  # Allow calculation with at least 1 valid value
    return x, moving_avg.tolist()

def plot_data():
    # Fetching data
    payrolls_x, payrolls_y = fetch_fred_data('PAYEMS')  # Total Nonfarm Payrolls
    wages_x, wages_y = fetch_fred_data('CES0500000003')  # Wages in the private sector

    # Calculate month-on-month change
    payrolls_x, payrolls_monthly_change = calculate_monthly_change(payrolls_x, payrolls_y)
    wages_x, wages_monthly_change = calculate_monthly_change(wages_x, wages_y)

    # Calculate 3-month moving average for wages
    wages_x, wages_moving_avg = calculate_moving_average(wages_x, pd.Series(wages_monthly_change), 3)

    # Latest datapoint for subtitles, rounded to the nearest decimal
    latest_payrolls = round(payrolls_monthly_change[-1], 1)
    latest_wages = round(wages_monthly_change[-1], 1)

    # Plotting payrolls data
    payroll_title = f'Monthly Changes in Payrolls, 1000s [{latest_payrolls}]'
    create_economic_chart(payrolls_x, [payrolls_monthly_change], 'Payrolls Data', payroll_title, 'Payrolls', ['Payrolls'], 'logo.jpg')

    # Plotting wages data including moving average
    wages_title = f'Monthly Changes in Wages and Moving Average [{latest_wages}]'
    create_economic_chart(wages_x, [wages_monthly_change, wages_moving_avg], 'Wages Data', wages_title, 'Wages', ['Wages', '3-Month Avg'], 'logo.jpg')

if __name__ == '__main__':
    plot_data()
