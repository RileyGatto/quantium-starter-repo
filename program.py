import pandas as pd

def clean_data(data):
    data['price'] = data['price'].replace({'\$':''}, regex=True).astype(float)
    return data
    # The backslash (\) is used to escape the dollar sign because $ is a special character in regular expressions.
    # regex=True: This parameter indicates that the keys in the dictionary should be treated as regular expressions. 
    # .astype(float): After the replacement, the resulting values are still strings. This method converts the modified price column to a numeric type (specifically, float).

def product_reduce(data):
    return data[data['product'] == "pink morsel"]

def total_sales(data):
    data['sales'] = data['price'] * data['quantity']
    return data
    # Can be left for last data = data.drop(columns=['price','quantity'])
    # Can reorder new_order = ['total_sales', 'product', 'price', 'quantity'


df1_0 = pd.read_csv('data/daily_sales_data_0.csv')
df2_0 = pd.read_csv('data/daily_sales_data_1.csv')
df3_0 = pd.read_csv('data/daily_sales_data_2.csv')

df1_1 = clean_data(df1_0)
df1_2 = product_reduce(df1_1);
df1_3 = total_sales(df1_2)

df2_1 = clean_data(df2_0)
df2_2 = product_reduce(df2_1);
df2_3 = total_sales(df2_2)

df3_1 = clean_data(df3_0)
df3_2 = product_reduce(df3_1);
df3_3 = total_sales(df3_2)

frame = [df1_3, df2_3, df3_3]

result = pd.concat(frame)

result = result.drop(columns=['product','price','quantity'])

result.to_csv('complete_sales_data.csv', index=False)





