import pandas as pd


def format_in_money(value):
    return f"${value:,.2f}"

def get_highest_gdp(data):
    # YOUR CODE HERE
    return data['GDP (USD)'].max()

def get_country_with_highest_gdp(data):
    # YOUR CODE HERE
    return data.loc[data['GDP (USD)'].idxmax()]['Country']

def get_italy_rows(data):
    # YOUR CODE HERE
    return data[data['Country'] == 'Italy']

data = pd.read_csv('./data/world_bank_dataset.csv')
data_by_country = data.sort_values('Year', ascending=False).groupby('Country')
for country, group in data_by_country:
    print(country)
    print(group)
    print('\n')
    
    
    
for country, group in data_by_country:
    print(country)
    for item in group.iterrows():
        print(f"Year: {item[1]['Year']}, GDP: {item[1]['GDP (USD)']}")
        print(f"Year: {item[1]['Year']}, GDP: {format_in_money(item[1]['GDP (USD)'])}")
    print('\n')
    
'''
for g in data_by_country.groups:
    print(g)
    
for g in data_by_country.groups:
    for row in data_by_country.get_group(g).iterrows():
        print("----------------------------")
        print(row)
'''


        
    