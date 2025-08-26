from __future__ import annotations
import pandas as pd
import numpy as np

def load_raw(train_path: str = 'data/raw/train.csv',
             test_path: str = 'data/raw/test.csv'):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Fix common inconsistencies
    if 'Item_Fat_Content' in df.columns:
        df['Item_Fat_Content'] = (df['Item_Fat_Content']
                                  .replace({'LF':'Low Fat','low fat':'Low Fat','reg':'Regular'}))
    # Handle missing values
    if 'Item_Weight' in df.columns:
        df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].median())
    if 'Outlet_Size' in df.columns:
        df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0])
    return df

def feature_engineer(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Example engineered features
    if 'Outlet_Establishment_Year' in df.columns:
        df['Outlet_Age'] = df['Outlet_Establishment_Year'].max() - df['Outlet_Establishment_Year']
    if 'Item_Visibility' in df.columns:
        df['Visibility_Sq'] = df['Item_Visibility'] ** 2
    if 'Item_MRP' in df.columns:
        df['MRP_Log'] = np.log1p(df['Item_MRP'])
    return df
