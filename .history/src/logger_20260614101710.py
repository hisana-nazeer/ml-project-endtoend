import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)