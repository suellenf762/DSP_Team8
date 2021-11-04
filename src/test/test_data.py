#!/bin/env python3
# To be filled by students
import unittest
from src.data import Dataset
import pandas as pd
import numpy as np





class TestData(unittest.TestCase):  
    def test_datetime(self):

        ## Create a test data frame with a mixture of datetime,number and text columns. With a duplicate row and missing values
       
        
        # initialise Dataset object - this includes all data in the CSV
        ds1 = da.Dataset()
        ds1.name = "my_test"
        
        ds1.df = {'text_column':  ['first_value', 'second_value', 'third_value','third_value','fifth_value',np.nan,np.nan],
        'number_column': [1,np.nan,3,4,5,6,6],
        'date_column1': [np.nan, '2/7/2020', '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        'date_column2': ['1-7-2020', '2-7-2020', '3/7/2020','4/7/2020','5/7/2020','6/7/2020','6/7/2020'],
        }
        
        ds1.df = pd.DataFrame(data)
        


        # test methods
        self.assertEqual(ds1.get_n_rows(),7)
        self.assertEqual(ds1.get_n_cols(),4)
        #self.assertEqual(ds1.get_cols_list(),1)
        #self.assertEqual(ds1.get_cols_dtype(),7)
        self.assertEqual(ds1.get_n_duplicates(),1)
        self.assertEqual(ds1.get_n_missing(),3)
        self.assertEqual(dc1.get_empty_1900(),1)
        self.assertEqual(dc1.get_empty_1970(),1)
        self.assertEqual(dc1.get_min(),pd.Timestamp("1900/01/01 00:00:00"))
        self.assertEqual(dc1.get_max(),pd.Timestamp("2022/01/13 13:01:02"))
        
        ### test on covid-19 sample csv ###
        csv_path = "01-01-2021_test.csv"
        
        if csv_path:
            # read csv
            df = pd.read_csv(csv_path)

            # init DateColumn
            dc2 = DateColumn()
            dc2.col_name = "Last_Update"
            dc2.serie = pd.to_datetime(df[dc2.col_name], dayfirst=True)

            # test methods
            print("Outputs using file",csv_path)
            print("get_name =",dc2.get_name())
            print("get_unique =",dc2.get_unique())
            print("get_missing =",dc2.get_missing())
            print("get_weekend =",dc2.get_weekend())
            print("get_weekday =",dc2.get_weekday())
            print("get_future =",dc2.get_future())
            print("get_empty_1900 =",dc2.get_empty_1900())
            print("get_empty_1970 =",dc2.get_empty_1970())
            print("get_min = ",dc2.get_min())
            print("get_max = ",dc2.get_max())

if __name__ == '__main__':
    unittest.main()