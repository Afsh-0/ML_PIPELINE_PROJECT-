#first we will gonna import the libraries 
import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


"""Now we will gonna create a class with name DataIngestionConfig and we know that in ingestion
we fetch data and later we split it so here also in the class first we will crate a path for 
train data and through this will create a folder artifacts and saved it as train.csv.
Similarly, we will have path for test data in folder artifacts with name test.csv and for raw data 
path in artifacts folder and stored it as raw.csv."""

@dataclass #decorator 
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def inititate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            logging.info("Data Reading using Pandas library from local system")
            data = pd.read_csv(os.path.join("notebook/data", "income_cleandata.csv"))
            logging.info("Data Reading Completed")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True) #creating a directory with name raw_data_path
            data.to_csv(self.ingestion_config.raw_data_path, index=True)#to save raw_data_path
            logging.info("Data splitted into train and test")

            train_set, test_set = train_test_split(data, test_size=0.30, random_state=1)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path)
            
        
        except Exception as e:
            logging.info("Error occured at Data Ingestion stage")
            raise CustmeException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.inititate_data_ingestion() #to check whether the code is currect or not 

"""now open your terminal and type
python https(-m src.components.data_ingestion) and you will see artifact folder as a output"""