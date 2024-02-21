import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from matplotlib import tight_layout

fetch_california_housing_data = fetch_california_housing()
x = fetch_california_housing_data.data
y = fetch_california_housing_data.target
data = pd.DataFrame(x, columns=fetch_california_housing_data.feature_names)
data["SellPrice"] = y
data.head()


print(fetch_california_housing_data.DESCR)
data.isnull().sum()
sns.pairplot(data,height=2.5)
plt.tight_layout()
sns.distplot(data["SellPrice"])
print("Skewness: %f" % data['SellPrice'].skew())
print("Kurtosis: %f" % data['SellPrice'].kurt())


