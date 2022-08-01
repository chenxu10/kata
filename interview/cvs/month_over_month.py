import pandas as pd
import psycopg2
import pandas.io.sql as sqlio

def get_df_from_sql():
    conn = psycopg2.connect(
        host="localhost",
        database="xushen",
        user="xushen",
        password="@12#311Bb")

    query = "select * from song"
    df = sqlio.read_sql_query(query, conn)
    return df

def aggregate_by_month(df):
    df["song_id"] = df["song_id"].astype(int)
    df["play_date"] = pd.to_datetime(df["play_date"])
    df["month"] = pd.DatetimeIndex(df["play_date"]).month
    df = df.groupby(["song_id","month"]).agg(
        {"number_of_plays":"sum"}
    ).reset_index()
    return df

def get_month_over_month():
    df = (get_df_from_sql().pipe(aggregate_by_month))
    return df

if __name__ == "__main__":
    df = get_month_over_month()
    print(df.info())
    print(df)

