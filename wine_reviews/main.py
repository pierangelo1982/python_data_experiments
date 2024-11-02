import pandas as pd

data = pd.read_csv('./data/winemag-data-130k-v2.csv')
# first 10 rows
print(data.head(10))
print("=====================================")
# lasts 10 rows
print(data.tail(10))
print("=====================================")
print("============ colums =================")
print("=====================================")
# show columns
print(data.columns)

print("=====================================")
print("===== highest point & lower point ===")
print("=====================================")

highest_point = data['points'].max()
print(f"Highest point: {highest_point}")
slower_point = data['points'].min()
print(f"Lower point: {slower_point}")

print("=====================================")
print("===== top wines ===")
print("=====================================")
top_wines = data[data['points'] == highest_point]
print(top_wines)

for index, row in top_wines.iterrows():
    print(f"{row['title']}\t{row['points']}\t{row['price']}\t{row['country']}\t{row['province']}\t{row['region_1']}\t{row['variety']}\t{row['winery']}")
    

print("=====================================")
print("=========== worst wines =============")
print("=====================================")
worst_wines = data[data['points'] == slower_point]
for index, row in worst_wines.iterrows():
    print(f"{row['title']}\t{row['points']}\t{row['price']}\t{row['country']}\t{row['province']}\t{row['region_1']}\t{row['variety']}\t{row['winery']}")

print("=====================================")
print("===== total wines by countries ======")
print("=====================================") 
wine_by_country = data.groupby('country').size().sort_values(ascending=False)
print(wine_by_country)

print("=====================================")
print("===== total wines by provinces ======")
print("=====================================")
wine_by_province = data.groupby('province').size().sort_values(ascending=False)
print(wine_by_province)

print("=====================================")
print("===== total wines by regions ======")
print("=====================================")
wine_by_region = data.groupby('region_1').size().sort_values(ascending=False)
print(wine_by_region)


