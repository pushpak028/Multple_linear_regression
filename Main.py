import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("\file_path")

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder = 'passthrough')
x = np.array(ct.fit_transfom(x))

x_train,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=0)

lr = Linear_regression()
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

np.setprintoptions(prcision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1)
