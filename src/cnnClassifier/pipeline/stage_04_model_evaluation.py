import sys
import os

# Add the 'src' directory to the path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_with_mlflow import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
