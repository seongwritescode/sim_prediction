import time
import os
from pathlib import Path
from datetime import datetime
from config_file import SIM_PREDICTION_HOME, LOGGING_FOLDER

class Logger:
    def __init__(self, verbose=True, to_file=True, log_file='log.txt', append=True):
        self.verbose = verbose
        self.to_file = to_file
        self.log_file = os.path.join(LOGGING_FOLDER, log_file)

        Path(os.path.join(LOGGING_FOLDER, log_file)).parent.mkdir(parents=True, exist_ok=True)
        if not append and os.path.exists(self.log_file):
            os.remove(self.log_file)

    def log(self, text):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if text:
            if self.verbose:
                print(date + ' ' + text)
            if self.to_file:
                with open(self.log_file, "a", encoding='utf8') as f:
                    f.write(date + ' ' + text)
                    f.write('\n')
