import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'






def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    query_string = f"(iso_a3 == '{country_code}' and '{year}'-01-01 and 12-31))"
    yearcountry_df = df.query(query_string)
    print(yearcountry_df['dollar price'])


          


def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    country_query = f"(iso_a3 == '{country_code}')"
    country_df = df.query(country_query)
    print(country_df)

def get_the_cheapest_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    cheapquery = f"(iso_a3 == '{year}')"
    print(cheapquery['dollar price'].min())

def get_the_most_expensive_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    expensivequery = f"(iso_a3 == '{year}')"
    print(expensivequery['dollar price'].max())

if __name__ == "__main__":
    pass # Remove this line and code your user interface