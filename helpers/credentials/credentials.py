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
    def __init__(self, filename: pathlib.Path) -> None:
        try:
            # create the credential parser
            configFile = configparser.ConfigParser()

            # read the file
            configFile.read(filename)

            # get the data
            self._username = configFile.get('credentials', 'username')
            self._password = configFile.get('credentials', 'password')
            self._service = configFile.get('instance', 'service')
            self._url = configFile.get('instance', 'url')
            self._port = configFile.getint('instance', 'port')
            self._sslRootCA = configFile.get('ssl', 'rootCA')
            self._sslCertificate = configFile.get('ssl', 'certificate')
            self._sslKey = configFile.get('ssl', 'key')
            self._database = configFile.get('database', 'name')

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
    def password(self) -> str:
        return self._password

    @property
    def service(self) -> str:
        return self._service

    @property
    def url(self) -> str:
        return self._url

    @property
    def port(self) -> int:
        return self._port

    @property
    def sslRootCA(self) -> str:
        return self._sslRootCA

    @property
    def sslCertificate(self) -> str:
        return self._sslCertificate

    @property
    def sslKey(self) -> str:
        return self._sslKey

    @property
    def database(self) -> str:
        return self._database
