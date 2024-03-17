"""
Zitadel
=======

Class to check Zitadel status.

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
class Zitadel:
    __instance = None
    _credentials = Credentials(CredentialLocations.zitadel)
    _healthCheckURL = f'{_credentials.url}:{_credentials.port}/healthz'

    ####################################################################################################################
    # PUBLIC METHODS ###################################################################################################
    ####################################################################################################################
    @classmethod
    def isHealthy(cls) -> dict:
        try:
            # get health status
            result = requests.get(cls._healthCheckURL)
            result.raise_for_status()

            # parse result
            result = result.json()
            if result.get('status').lower() == 'serving':
                isHealthy = True
                message = 'Zitadel is operational.'
            else:
                isHealthy = False
                message = 'Zitadel is not operational.'

            # return dict
            return {'isReady': isHealthy, 'message': message}

        except Exception as e:
            raise RuntimeError(f'Zitadel Health Check - Error message: {e}')

    ####################################################################################################################
    # CONSTRUCTOR ######################################################################################################
    ####################################################################################################################
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super()
        return cls.__instance