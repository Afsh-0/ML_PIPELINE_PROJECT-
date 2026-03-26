from src.logger import logging
from src.exception import CustmeException
import os, sys
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_curve, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV

"""now we will define a function to save a pkl file and inside it first we will define a path and second call an object and in next 
stage will will define a path as dir_path and later we will create a dir of that path and after that we will open it in wb mode which 
is write mode and dump a pickle file there in obj from file_obj"""
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustmeException(e, sys)

           #now go to data_transformation.py to save pkl in file

def evaluate_model(x_train, y_train, x_test, y_test, model, params):
    try:
        report = {}
        for i in range(len(list(model))):
            model_value = list(model.values())[i]
            model_param = params[list(model.keys())[i]]

            GS = GridSearchCV(model_value, model_param, cv=5)
            GS.fit(x_train, y_train)

            best_model_estimator = GS.best_estimator_

            y_pred = best_model_estimator.predict(x_test)
            test_model_accuracy = accuracy_score(y_test, y_pred)

            report[list(model.values())[i]] = test_model_accuracy

        return report 
        
    except Exception as e:
        raise CustmeException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustmeException(e, sys)

