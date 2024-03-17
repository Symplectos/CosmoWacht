"""
Credentials
===========

Configuration parser for credential files.

:Authors:
    Gilles Bellot
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
import configparser
import pathlib


########################################################################################################################
# DEFINITIONS ##########################################################################################################
########################################################################################################################

########################################################################################################################
# CLASS ################################################################################################################
########################################################################################################################
class Credentials:
    ####################################################################################################################
    # CONSTRUCTOR ######################################################################################################
    ####################################################################################################################
    def __init__(self, filename: pathlib.Path):
        try:
            # variables
            self._url, self._port, self._username = None, None, None

            # create the credential parser
            configFile = configparser.ConfigParser()

            # read the file
            configFile.read(filename)

            # get the data
            if configFile.has_section('credentials'):
                # get the credentials
                if configFile.has_option('credentials', 'username'):
                    self._username = configFile.get('credentials', 'username')

            if configFile.has_section('instance'):
                # get instance
                if configFile.has_option('instance', 'url'):
                    self._url = configFile.get('instance', 'url')
                if configFile.has_option('instance', 'port'):
                    self._port = configFile.getint('instance', 'port')

        except configparser.Error as e:
            raise e

        except Exception as e:
            raise RuntimeError(e)

    ####################################################################################################################
    # GETTERS#### ######################################################################################################
    ####################################################################################################################
    @property
    def username(self) -> str:
        return self._username

    @property
    def url(self) -> str:
        return self._url

    @property
    def port(self) -> int:
        return self._port
