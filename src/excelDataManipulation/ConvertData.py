import pandas as pd
import numpy as np

def convertData(inputFile, outputFile):
    # Create a MultiIndex
    df = pd.read_excel(inputFile, sheet_name = 'input_refresh_template', header=[1, 1], index_col=0, skiprows=1)

    # Delete duplicate columns
    df = df.drop_duplicates()

    # Rename axis
    df = df.rename_axis(columns=['Date', None], index='Site ID')


    # Pivot your dataframe
    df = df.stack(level='Date').reset_index()

    # print the values
    print(df)

    # Save value to excel
    df.to_excel(outputFile, sheet_name = 'output_31_days_report')

