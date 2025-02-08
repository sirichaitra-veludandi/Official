import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

df 

df_new = df.drop(["Model","Fuel_Type"],axis=1,inplace=True)

df.drop(["Color"],axis=1,inplace=True)
df.corr

df.corr()

import statsmodels.formula.api as smf
model = smf.ols('Price~Mfg_Year+Central_Lock+Powered_Windows',data=df).fit()
(model.rsquared,model.rsquared_adj)