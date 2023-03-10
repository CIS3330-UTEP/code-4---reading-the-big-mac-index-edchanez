import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'


#This is my comment



def get_big_mac_price_by_year(year,country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    query_string = f"(iso_a3 == '{country_code}' and date >= '{year}-01-01' and date <= '{year}-12-31')"
    yearcountry_df = df.query(query_string)
    result = yearcountry_df['dollar_price'].mean()
    result = round(result,2)
    return result


          


def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    df = pd.read_csv(big_mac_file)
    country_query = f"(iso_a3 == '{country_code}')"
    country_df = df.query(country_query)
    result = country_df['dollar_price'].mean()
    result = round(result,2)
    return result

def get_the_cheapest_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    cheapquery = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    year_df = df.query(cheapquery)
    resultindex = year_df['dollar_price'].idxmin()
    # print(resultindex)
    # print(type(resultindex))
    minrow = year_df.loc[resultindex]
    # print(minrow)
    roundresult = round(minrow['dollar_price'],2)
    result = f"{minrow['name']}({minrow['iso_a3']}): ${roundresult}"
    # print(result)

    # print(result)
    # result = round(result,2) 
    return result

def get_the_most_expensive_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    expensivequery = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    expyear_df = df.query(expensivequery)
    resultindex = expyear_df['dollar_price'].idxmax()
    maxrow = expyear_df.loc[resultindex]
    result = f"{maxrow['name']}({maxrow['iso_a3']}): ${round(maxrow['dollar_price'],2)}"

    return result

    

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2001,'mex'))
    print(get_big_mac_price_by_country('mex'))
    print(get_the_cheapest_big_mac_price_by_year(2000))
    print(get_the_most_expensive_big_mac_price_by_year(2001))

    
