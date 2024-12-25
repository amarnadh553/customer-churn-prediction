import os
import pandas as pd
from dataclasses import dataclass

from sklearn.model_selection import train_test_split



from customer_churn.utils.utilities import create_folder
from customer_churn.exceptions import CustomException


DATA_FOLDER_NAME='artifacts'

@dataclass
class DataIngestionConfig:

    raw_data_path:str = os.path.join("artifacts", "raw.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        try:
            
            # Read the raw data
            file_path=r'data/Customer-Churn.csv'
            df = pd.read_csv(file_path)

            # Create a folder to store the artifacts
            parent_dir = os.getcwd()+os.sep+"customer_churn"
            raw_set_path = os.path.basename(self.ingestion_config.raw_data_path)
            train_set_name = os.path.basename(self.ingestion_config.train_data_path)
            test_set_name = os.path.basename(self.ingestion_config.test_data_path)

            # Create the folder if it does not exist
            create_folder(parent_dir+os.sep+DATA_FOLDER_NAME)

            # Save the raw data to the artifacts folder
            df.to_csv(parent_dir+os.sep+DATA_FOLDER_NAME+os.sep+raw_set_path, index=False)

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.20, random_state=20)
            train_set.to_csv(parent_dir+os.sep+DATA_FOLDER_NAME+os.sep+train_set_name, index=False)
            test_set.to_csv(parent_dir+os.sep+DATA_FOLDER_NAME+os.sep+test_set_name, index=False)

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except CustomException as ce:
            print(f"Custom Excepion : {ce.message}")
            if ce.details:
                print(f"Details : {ce.details}")

            
        except Exception as e:
            raise CustomException("An error occurred during data ingestion.", details=str(e))

if __name__ == "__main__":

    try:
        obj = DataIngestion()
        temp = obj.initiate_data_ingestion()
        print(temp)
    except CustomException as e:
        print(f"Error: {e.message}")
        if e.details:
            print(f"Details: {e.details}")
