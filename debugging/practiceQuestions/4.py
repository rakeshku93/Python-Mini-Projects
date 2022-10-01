# Q4. What are the two lines that your program must have in order to be able to call logging.debug()?

import logging
logging.basicConfig(filename="programLog.txt", 
                    level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s -  %(message)s")