import os
import sys
import mlflow
import mlflow.keras as mlk
import logging
from pathlib import Path

#import core.utils.utilities as utilities
from core.utils.Utilities import Utilities

class ModelUtilities:
    logger = logging.getLogger(__name__)
    def __init__(self) -> None:
        pass
        print("Logger",self.logger)
        source_path = str(Path("./").resolve())
        sys.path.append(source_path) 
    
    def test_mlflow(self):
        utilities=Utilities()
        os.environ["MLFLOW_S3_ENDPOINT_URL"] = utilities.get_value("MINIO.MLFLOW_S3_ENDPOINT_URL","../resources/config/config.json") # api 9000
        os.environ["AWS_ACCESS_KEY_ID"] = utilities.get_value("MINIO.AWS_ACCESS_KEY_ID","../resources/config/config.json")
        os.environ["AWS_SECRET_ACCESS_KEY"] = utilities.get_value("MINIO.AWS_SECRET_ACCESS_KEY","../resources/config/config.json")
        tracking_uri = utilities.get_value("MLFLOW.MLFLOW_TRACKING_URL","../resources/config/config.json")

        try:
            mlflow.set_tracking_uri(tracking_uri)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            raise e

        try:
            mlflow.set_experiment("TEST",)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            raise e

        with mlflow.start_run():
            pass


    def log_model(self,experiment, model, lib, metrics=None, params=None, artefacts=None):

        """
        A utiity function for logging model in MlFlow

        :param experiment: Experiment name
        :param params: Any hyper parameters
        :param metrics: Performance metrics
        :return:
        """
        utilities=Utilities()
        os.environ["MLFLOW_S3_ENDPOINT_URL"] = utilities.get_value("MINIO.MLFLOW_S3_ENDPOINT_URL","../resources/config/config.json") # api 9000
        os.environ["AWS_ACCESS_KEY_ID"] = utilities.get_value("MINIO.AWS_ACCESS_KEY_ID","../resources/config/config.json")
        os.environ["AWS_SECRET_ACCESS_KEY"] = utilities.get_value("MINIO.AWS_SECRET_ACCESS_KEY","../resources/config/config.json")
        tracking_uri = utilities.get_value("MLFLOW.MLFLOW_TRACKING_URL","../resources/config/config.json")

        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment(experiment)

        with mlflow.start_run():

            if params:
                for param in params:
                    mlflow.log_param(param, params[param])
                print("Parameters were logged !!!")

            if metrics:
                for metric in metrics:
                    mlflow.log_metric(metric, metrics[metric])
                print("Performance metrices were logged !!!")

            if artefacts:
                for arte in artefacts:
                    mlflow.log_artefact(arte)
                print("Artefacts were logged !!!")

            if lib.lower() == 'keras':
                print("Keras model logged successfully !!!")
                mlk.log_model(model, "model", registered_model_name="CNN5 Model",lib='keras')
            else:
                raise "only keras models allowed"