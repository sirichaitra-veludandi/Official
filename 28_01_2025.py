import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
data = {
    "customer_id": [1,2,3,4],
    "gender": ["Male","Female","Female","Male"],
    "subscription_status": ["Active","Inactive","Active","Inactive"]
}
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)