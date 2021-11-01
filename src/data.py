# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd




@dataclass
class Dataset():
  name: str =None
  df: pd.DataFrame =None



  def get_name(self):
    """
    Return filename of loaded dataset
    """
    return None

  def get_n_rows(self):
    """
      Return number of rows of loaded dataset
    """
    return str(self.shape[0])

  def get_n_cols(self):
    """
      Return number of columns of loaded dataset
    """
    return str(df.shape[1])

  def get_cols_list(self):
    """
      Return list column names of loaded dataset
    """
    return None

  def get_cols_dtype(self):
    """
      Return dictionary with column name as keys and data type as values
    """
    return pd.DataFrame(self.dtypes, columns=['Type'])

  def get_n_duplicates(self):
    """
      Return number of duplicated rows of loaded dataset
    """
    return self[self.duplicated()]

  def get_n_missing(self):
    """
      Return number of rows with missing values of loaded dataset
    """
    return str((self.isna().sum(axis=1) > 0).sum())

  def get_head(self, n=5):
    """
      Return Pandas Dataframe with top rows of loaded dataset
    """
    return None

  def get_tail(self, n=5):
    """
      Return Pandas Dataframe with bottom rows of loaded dataset
    """
    return None

  def get_sample(self, n=5):
    """
      Return Pandas Dataframe with random sampled rows of loaded dataset
    """
    return None

  def get_numeric_columns(self):
    """
      Return list column names of numeric type from loaded dataset
    """
    return None

  def get_text_columns(self):
    """
      Return list column names of text type from loaded dataset
    """
    return None

  def get_date_columns(self):
    """
      Return list column names of datetime type from loaded dataset
    """
    return None

