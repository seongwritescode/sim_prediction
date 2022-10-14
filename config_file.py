import os

import pathlib


class SimPredictionConfigParser:
    def get_lead_scoring_home(self):
        path = pathlib.Path(__file__).parent.resolve()
        return path

    def get_rules_based(self):
        pass

    def load_rules_db(self):
        pass






sim_prediction_config = SimPredictionConfigParser()
SIM_PREDICTION_HOME = sim_prediction_config.get_lead_scoring_home()
DATA_PATH = os.path.join(SIM_PREDICTION_HOME,'data')
LOGGING_FOLDER = os.path.join(SIM_PREDICTION_HOME, 'log')

