import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
datf = pd.DataFrame({"Season 1": [7,4,5,6,3],
"Season 2": [1,2,8,4,9]})
p = sns.histplot(data = datf)
p.set(xlabel="X Label value",ylabel = "Y Label Value")
plt.show() 



import matplotlib.pyplot as plt
data = [5 ,7, 7, 8, 9, 10, 10, 10, 11, 1211,11]
plt.hist(data, bins=10,edgecolor='black')
plt.title('simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
np.random.randint(20,82,240)
plt.hist(data, bins=15, edgecolor='black', color='lightblue')
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')