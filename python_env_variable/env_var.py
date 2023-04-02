"""Env dataclass to load and hold all environment variables
"""
import os
from dotenv import load_dotenv, find_dotenv

class Env:
    """Loads all environment variables into a predefined set of properties
    """
    def __init__(self, environment):
        # to load .env file into environment variables execution
        load_dotenv(find_dotenv(f"./.{environment}.env"))
        
        for env in os.environ.items():
            # access and manipulate instance variables 
            self.__dict__[env[0].lower()] = env[1]
            
if __name__ == "__main__":
    print("ENV Variables loaded...")
    environment_variables = Env("exp")
    
    print(environment_variables.__dict__)