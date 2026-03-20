import os, sys
from src.logger import logging


"""we have created a function with name error_message_detailed(can choose any name) with parameters
defined error and error_detailed"""
def error_message_detailed(error, error_detaild:sys):
    _, _, exc_tb = error_detaild.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message ="An Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

"""we want only third parameter which is exc_tb which a function of exception handling not first two.
when we will gonna run a codees of pipeline and components, there will be a 1000s lines codes and
exc_tb is the exception from try block and will gonna read code from 1 to 1000s and exc_info() is the
information of an error."""
""""f_code will show exactly at which code you will gonna have an error and co_filename will
gonna run try and except for every folders files subfolders and subfiles."""
"""now we will gonna define an variable with name error_message which will show a message when
exception will arise, line number in the form of str"""

class CustmeException(Exception):
    def __init__(self, error_message, error_detailed:sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message, error_detaild = error_detailed)
    
    def __str__(self):
        return self.error_message    

if __name__ == "__main__":
    try:
        a = 1/0

    except Exception as e:
        logging.info("Division by zero")
        raise CustmeException(e, sys)