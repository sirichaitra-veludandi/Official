import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name) 

car_new = pd.DataFrame({'HP':20,"VOL":75,"SP":100,"WT":25},index=[1])

final_ml_v.predict(car_new)

final_ml_v.predict(car_new.iloc[0:5])

pred_y = final_ml_v.predict(car_new)
pred_y

final_ml_v.rsquared,final_ml_w.aic