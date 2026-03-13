from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataingestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.data_transformation import DataTransformation
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

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("initiate the data transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")
        print(data_transformation_artifact)






        

    except Exception as e:
           raise NetworkSecurityException(e,sys)