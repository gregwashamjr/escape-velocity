import pandas as pd

def load_debts(path="data/debts.csv"):
    df = pd.read_csv(path)

    # Force numeric types (THIS is the fix)
    df["Balance"] = pd.to_numeric(df["Balance"])
    df["APR"] = pd.to_numeric(df["APR"])
    df["Minimum"] = pd.to_numeric(df["Minimum"])

    return df


def total_debt(df):
    return df["Balance"].sum()


def avalanche_order(df):
    return df.sort_values("APR", ascending=False).reset_index(drop=True)


def next_target(df):
    return avalanche_order(df).iloc[0]