"""
Configuration file. Reads data from a .env file in the root of the installation directory.
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
from dataclasses import dataclass
import os
import pathlib
from dotenv import load_dotenv

########################################################################################################################
# LOAD ENVIRONMENT VARIABLES ###########################################################################################
########################################################################################################################
pathToBaseDirectory = pathlib.Path().absolute()
load_dotenv(pathToBaseDirectory.joinpath('.env'))


########################################################################################################################
# CLASS ################################################################################################################
########################################################################################################################
@dataclass(frozen=True)
class Config(object):
    webroot = os.environ.get('WEBROOT', '')
    title = os.environ.get('TITLE', 'CosmoWacht')
    header = os.environ.get('HEADER', 'Global Status')