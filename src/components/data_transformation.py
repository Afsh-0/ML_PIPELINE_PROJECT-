#Once an EDA is done we move to data transformation

import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer #Imputer fills the null values
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.utils import save_object #afer utlis.py 

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts/data_transformation", "preprocessor.pkl")
    #this will create an pkl with name preprocessor inside artificates folder inside data_trasformation folder once model is being build

"""Now well create an variable num_pipline to call a pipline and in this we need to define the steps
     like in imputer we are doing SimpleImputer and select stragey as Median to fill a null values and next
     next step is to scaled it and do same steps for cat_pipline too if you have a categorical data but  
     don't scaled it as we don't scale cat values."""

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformation_obj(self):
        try:
            logging.info("Data Transformation has started")

            numerical_features = numerical_features = ["age", "education_num", "capital_gain", "capital_loss", "hours_per_week"]

            num_pipeline = Pipeline(steps= [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
            
            preprocessor = ColumnTransformer([("num_pipeline", num_pipeline, numerical_features)])

            return preprocessor

        except Exception as e:
            raise CustmeException(e, sys)

        """ to remove an outlier we are defining a function with IQR method"""

    def remove_outliers_IQR(self, col, df): 
        try:
            df[col] = df[col].astype(float)

            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)

            iqr = Q3 - Q1

            upper_limit = Q3 + 1.5*iqr
            lower_limit = Q1 - 1.5*iqr

            df.loc[(df[col]>upper_limit),col] =upper_limit
            df.loc[(df[col]<lower_limit),col] =lower_limit

            return df 
      
        except Exception as e:
            logging.info("Outlier handing code")
            raise CustmeException(e, sys)
      

        """you need to define an function if data is not endcoded but ours is so we will 
          skip but if it not then please define a function for data encoding"""

        """now, we will define a function to initiate data transformation and it is initiate on train  and
          test path and after reading it we will run an loop for outlier filing and inbetween add a logging
          to have a track of an error"""

    def inititate_data_transformation(self, train_path, test_path):
        try:
            train_data = pd.read_csv(train_path) #first we will read it
            test_data = pd.read_csv(test_path)

            numerical_features = ["age", "education_num", "capital_gain", "capital_loss", "hours_per_week"]

            train_data.columns = train_data.columns.str.strip()
            test_data.columns = test_data.columns.str.strip()
        
            for col in numerical_features:
                self.remove_outliers_IQR(col=col, df=train_data)

            logging.info("outliers capped on our train data")

            for col in numerical_features:
                self.remove_outliers_IQR(col=col, df=test_data)
        
            logging.info("outliers capped on our test data")

            preprocessor_obj = self.get_data_transformation_obj() #define a variable to call a function

            target_columns = "income"

            drop_columns = [target_columns] #to define x and y

            logging.info("splitting train data into dep and indep variables")
            input_feature_train_data = train_data.drop(drop_columns, axis =1)
            target_feature_train_data = train_data[target_columns]

        
            logging.info("splitting test data into dep and indep variables")
            input_feature_test_data = test_data.drop(drop_columns, axis =1)
            target_feature_test_data = test_data[target_columns]

            #to apply transformation on train and test data
            input_train_arr = preprocessor_obj.fit_transform(input_feature_train_data)
            input_test_arr = preprocessor_obj.transform(input_feature_test_data)

            train_array = np.c_[input_train_arr, np.array(target_feature_train_data)]
            test_array = np.c_[input_test_arr, np.array(target_feature_test_data)]

            #after utils.py
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessor_obj)
        
            return(train_array, test_array, self.data_transformation_config.preprocessor_obj_file_path)
    

        except Exception as e:
            raise CustmeException(e, sys)


     
