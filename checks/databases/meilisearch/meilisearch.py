"""
MeiliSearch
===========

Class to check MeiliSearch status.

:Authors:
    Gilles Bellot
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
import requests
from helpers import Credentials, CredentialLocations


########################################################################################################################
# DEFINITIONS ##########################################################################################################
########################################################################################################################

########################################################################################################################
# CLASS ################################################################################################################
########################################################################################################################
class MeiliSearch:
    __instance = None
    _credentials = Credentials(CredentialLocations.meiliSearch)
    _healthCheckURL = f'{_credentials.url}:{_credentials.port}/health' if _credentials.port is not None \
                      else f'{_credentials.url}/health'

    ####################################################################################################################
    # PUBLIC METHODS ###################################################################################################
    ####################################################################################################################
    @classmethod
    def isHealthy(cls) -> dict:
        try:
            # get health status
            result = requests.get(cls._healthCheckURL)

            if result.status_code != 200:
                isHealthy = False
                message = 'MeiliSearch is not operational.'
            else:
                # parse result
                result = result.json()
                if result.get('status').lower() == 'available':
                    isHealthy = True
                    message = 'MeiliSearch is operational.'
                else:
                    isHealthy = False
                    message = 'MeiliSearch is not operational.'

            return {'isHealthy': isHealthy, 'message': message, 'serviceName': cls.__name__}

        except Exception as e:
            raise RuntimeError(f'MeiliSearch Health Check - Error message: {e}')

    ####################################################################################################################
    # CONSTRUCTOR ######################################################################################################
    ####################################################################################################################
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super()
        return cls.__instance
