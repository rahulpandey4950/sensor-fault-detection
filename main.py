from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from dotenv import load_dotenv

envfile = ".env"
BASEDIR= os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, envfile))

if __name__ == '__main__':
    try:
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise e