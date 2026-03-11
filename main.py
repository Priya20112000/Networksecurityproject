from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataingestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataingestionConfig(trainingpipelineconfig)
        
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("data initiation completed")
        print(dataingestionartifact)
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        datavalidation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("initiate the data validation")
        data_validation_artifact=datavalidation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)
        

    except Exception as e:
           raise NetworkSecurityException(e,sys)