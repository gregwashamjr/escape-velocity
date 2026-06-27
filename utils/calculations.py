import pandas as pd

def load_debts(path="data/debts.csv"):
    return pd.read_csv(path)


def total_debt(df):
    return df["Balance"].sum()


def avalanche_order(df):
    return df.sort_values("APR", ascending=False).reset_index(drop=True)


def next_target(df):
    return avalanche_order(df).iloc[0]