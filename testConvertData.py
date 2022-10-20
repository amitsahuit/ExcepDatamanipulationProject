import pytest
import pandas as pd
import datatest as dt
from numbers import Number

inputFile = './/sampleInOutFiles//InpFile.xlsx'

@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    # Create a MultiIndex
    df = pd.read_excel(inputFile, sheet_name = 'input_refresh_template', header=[1, 1], index_col=0, skiprows=1)

    # Delete duplicate columns
    df = df.drop_duplicates()
    
    # Rename axis
    df = df.rename_axis(columns=['Date', None], index='Site ID')

    # Pivot your dataframe
    df = df.stack(level='Date').reset_index()

    #delete unwanted rows
    df.dropna(axis=0,how='any',subset=None,inplace=True)
    
    return df


# @pytest.mark.mandatory
def test_columns(df):
    dt.validate(
        df.columns,
        {'Site ID','Date','Average Time Spent on Site','Page Views','Total Time Spent','Unique Visitors','Visits'},
    )

def test_site_id(df):
    dt.validate.subset(
        df['Site ID'],
        {'site 1','site 2','site 3','site 4','site 5','site 6','site 7','site 8','site 9','site 10','site 11','site 12','site 13','site 14','site 15','site 16','site 17','site 18','site 19','site 20','site 21','site 22','site 23','site 24','site 25','site 26','site 27','site 28','site 29','site 30','site 31','site 32','site 33','site 34','site 35','site 36','site 37','site 38','site 39','site 40','site 41','site 42','site 43','site 44','site 45','site 46','site 47','site 48','site 49','site 50','site 51','site 52','site 53','site 54','site 55','site 56','site 57','site 58','site 59','site 60','site 61','site 62','site 63','site 64','site 65','site 66','site 67','site 68','site 69','site 70','site 71','site 72','site 73','site 74','site 75','site 76','site 77','site 78','site 79','site 80','site 81','site 82','site 83','site 84','site 85','site 86','site 87','site 88','site 89','site 90','site 91','site 92','site 93','site 94','site 95','site 96','site 97','site 98','site 99','site 100'},
    )
    
def test_date(df):
    dt.validate(df['Date'], pd.Timestamp)

def test_average_Time_Spent_on_Site(df):
    dt.validate(df['Average Time Spent on Site'], Number)
                    
def test_pageViews(df):
    dt.validate(df['Page Views'], int)

def test_totalTimeSpent(df):
    dt.validate(df['Total Time Spent'], int)
    
def test_uniqueVisitors(df):
    dt.validate(df['Unique Visitors'], int)

def test_visits(df):
    dt.validate(df['Visits'], int)