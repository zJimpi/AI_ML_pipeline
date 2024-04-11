import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass



## Step1: Create path variables to store the files are raw csv
@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('../../artifacts','train.csv')
    test_data_path:str=os.path.join('../../artifacts','test.csv')
    raw_data_path:str=os.path.join('../../artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        print("inside initiate ingestion")
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('../../data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            # its just the path.... here we create the folder ..b/c in to_csv cant create a file inside folder ..we need to have the folder
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)#raw.csv is created  path =artifacts\raw.csv
            
            logging.info('Train test split')
            
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#train.csv created  path=artifacts\train.csv
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)# test.csv created  path=artifacts\test.csv

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,# returing thes file path for the next moule to use
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        
#testing
# obj = DataIngestion()
# obj.initiate_data_ingestion()