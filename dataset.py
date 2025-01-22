import pandas as pd
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerId': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
sales_df = pd.DataFrame(sales_data)

customer_data = {
    'CustomerId': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
customer_df = pd.DataFrame(customer_data)
merged_df = pd.merge(sales_df, customer_df, on='CustomerId', how='inner')

print("\nMerged DataFrame:")
print(merged_df) 



import pandas as pd
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerId': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
sales_df = pd.DataFrame(sales_data)

customer_data = {
    'CustomerId': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
customer_df = pd.DataFrame(customer_data)
merged_df = pd.merge(sales_df, customer_df, on='CustomerId', how='right')
print("\nMerged DataFrame:")
print(merged_df)



import pandas as pd
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerId': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
sales_df = pd.DataFrame(sales_data)

customer_data = {
    'CustomerId': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
customer_df = pd.DataFrame(customer_data)
merged_df = pd.merge(sales_df, customer_df, on='CustomerId', how='inner')

print("\nMerged DataFrame:")
print(merged_df)



import pandas as pd
sales_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'CustomerId': [101, 102, 103, 104, 101],
    'Amount': [250, 300, 400, 500, 600],
    'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05']
}
sales_df = pd.DataFrame(sales_data)

customer_data = {
    'CustomerId': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [30, 35, 40, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
customer_df = pd.DataFrame(customer_data)
merged_df = pd.merge(sales_df, customer_df, on='CustomerId', how='outer')

print("\nMerged DataFrame:")
print(merged_df)