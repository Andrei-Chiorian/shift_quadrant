import pandas as pd
import numpy as np

if __name__ == '__main__':

    def __init__(self, nombre, edad):

    shift = {
        'Ma': 'Ma',
        'Ta': 'Ta',
        'No': 'No',
        'Li': 'Li'
    }

    employees = ['Andrei', 'Irina', 'Lucas', 'Abraham']

    month = 10
    year = 2024
    # print(f'{month:02d}')

    days_month = pd.date_range(start=f'{year}-{month:02d}-01',
                        end=pd.Timestamp(f'{year}-{month:02d}-01') + pd.offsets.MonthEnd(1))

    shift_quadrant = pd.DataFrame(columns=days_month.day, index=employees)

    print(shift_quadrant.to_markdown())
