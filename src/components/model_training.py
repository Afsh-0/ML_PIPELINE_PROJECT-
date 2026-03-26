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
from src.utils import save_object 
from src.utils import evaluate_model #after utils.py


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

"""first we will gonna create a class with name ModelTrainingConfig and inside it, first we will 
a variable and inside it we will define a file path and file which is to be created like
we are creating a folder model_training inside artifacts and after training it will be stored inside 
it as model.pkl"""

@dataclass
class ModelTrainingConfig:
    train_model_file_path = os.path.join("artifacts/model_training", 'model.pkl')

class ModelTraining:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()
    
    def inititate_model_training(self, train_array, test_array):
        try: # we are defining here a data of train and test array
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            """Now we will define all models that we will use in training"""

            model = {
                "Random Forest": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                "Logistic Regression": LogisticRegression()
            }

            """We will gonna do the tunning so we will define a params"""

            params = {
                "Random Forest": {
                    "class_weight": ['balanced'],
                    "n_estimators": [20, 50, 30],
                    "max_depth": [10, 8, 5],
                    "min_samples_split": [2, 5, 10]
                },

                "Decision Tree": {
                    "class_weight": ['balanced'],
                    "criterion": ['gini', 'entropy', 'log_loss'],
                    "splitter": ['best', 'random'],
                    "max_depth": [3, 4, 5, 6],
                    "min_samples_split": [2, 3, 4, 5],
                    "min_samples_leaf": [1, 2, 3],
                    "max_features": ['auto', 'sqrt', 'log2']
                },

                "Logistic Regression": {
                    "class_weight": ['balanced'],
                    "penalty": ['l1', 'l2'],
                    "C": [0.001, 0.01, 0.1, 1, 10, 100],
                    "solver": ['liblinear', 'saga']
                }
            }
                  #after utils.py
            model_report: dict = evaluate_model(x_train=x_train, y_train=y_train, x_test=x_test, 
                                                y_test=y_test, model=model, params=params)
            #now we will create an variable which will give me best score 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = model[best_model_name]

            logging.info(f"best model found, Model name is {best_model_name}, accuracy score: {best_model_score}")
            

            #to save it as a pkl file
            save_object(file_path=self.model_training_config.train_model_file_path,
                        obj = best_model
                        )
            
        except Exception as e:
            raise CustmeException(e, sys) 