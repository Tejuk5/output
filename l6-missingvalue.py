import os
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

file_path = os.path.join("datasets","housing","housing.csv")
housing = pd.read_csv(file_path)
print("####################################################################")
print("printing housing dataset information\n")
print(housing.info())


imputer = SimpleImputer(strategy = "median")
housing_num  =housing.drop("ocean_proximity",axis=1)
imputer.fit(housing_num)
print("printing the content of statistics_ variable after executing fir function\n")
print(imputer.statistics_)
X = imputer.transform(housing_num)
housing_tr=pd.DataFrame(X,columns=housing_num.columns,index=housing_num.index)
print("########################################################################")
print("printing housing dataset information after transformation\n")
print(housing_tr.info())
print("tranformed housing dataset contents\n")
print(housing_tr)

housing_cat = housing[["ocean_proximity"]]
print("first 10 instance in housing dataset ocean_proximity attribute values\n")
print(housing_cat.head(10))


cat_encoder = OneHotEncoder()
housing_cat_1Hot = cat_encoder.fit_transform(housing_cat)
print("contents of one hot encoder after transformation on housing datasets ocean_proximity attribute\n")
print(housing_cat_1Hot.toarray())
print("\ncategories of onhotencoder:\n")
print(cat_encoder.categories_)

new_housing = housing.drop(['ocean_proximity'],axis=1)
print("housing dataset content without ocean proximity column in order to be converted to scaled value", new_housing.head())
scaler = StandardScaler()
scaled_data = scaler.fit_transform(pd.DataFrame(new_housing))
scaled_df=pd.DataFrame(scaled_data,columns=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house-value'])
print("top 5 instance contents of the dataset after dataset has been scaled using standard scalar")
print(scaled_df.head())