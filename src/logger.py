"""suppose, we are writting a code of thousand lines and what if errors comes in between. so 
for that we are writting codes between logs and through this we can check where we are having an error
and can fix it there. Like is it between data ingestion or validation."""

import os
import sys
import logging
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
"""we have defined an variable where we are running all files but in between logs and 
keeping a track of time in preferred formate."""

"""Now we will defined a new variable where we can store logs data. So we have defined a 
function name log_path to show the path of log file which is current directory and we will get 
by os.get.cwd() function and logs is folder we have created to log file and it will 
be store in the formate mentioned in the vairable LOG_FILE."""

log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(log_path, exist_ok=True) #we have created a file logs within a directory 

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO #we are collecting all infor here 
)

"""asctime will show the time when an error will occur and lineno means at which line and message
to show what error"""

"""now, to check whether are logs properly working or not we will do"""

#if __name__ == "__main__":
#    logging.info("Loggin started") 