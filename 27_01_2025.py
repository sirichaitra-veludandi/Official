import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = {
    "age": [25,30,35,40,45],
    "height": [150,160,170,180,190],
    "weight": [50,60,70,80,90],
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
print(scaled_df)



import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "age": [25, 30, 35, 40, 45],
    "height": [150, 160, 170, 180, 190],
    "weight": [50, 60, 70, 80, 90],
}

df = pd.DataFrame(data)
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
print(normalized_df)



import pandas as pd
from sklearn.preprocessing import StandardScaler
data = {
    "age": [25, 30, 35, 40, 45],
    "height": [150, 160, 170, 180, 190],
    "weight": [50, 60, 70, 80, 90],
    "income": [3000, 4000, 5000, 6000, 7000],
}
df = pd.DataFrame(data)
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df_standardized)