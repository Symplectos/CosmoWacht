"""
PostgreSQL
==========

Class to check PostgreSQL database status.

:Authors:
    Gilles Bellot
"""

########################################################################################################################
# IMPORTS ##############################################################################################################
########################################################################################################################
import subprocess
from helpers import Credentials, CredentialLocations


########################################################################################################################
# DEFINITIONS ##########################################################################################################
########################################################################################################################

########################################################################################################################
# CLASS ################################################################################################################
########################################################################################################################
class PostgreSQL:
    __instance = None
    _credentials = Credentials(CredentialLocations.postgreSQL)

    ####################################################################################################################
    # PUBLIC METHODS ###################################################################################################
    ####################################################################################################################
    @classmethod
    def isHealthy(cls) -> dict:
        try:
            isReady, message = True, None

            # use subprocess to query the PostgreSQL status
            command = 'pg_isready'
            options = (f"-d 'postgresql://{cls._credentials.username}@"
                       f"{cls._credentials.url}:{cls._credentials.port}'") if cls._credentials.port is not None else \
                f"-d 'postgresql://{cls._credentials.username}@{cls._credentials.url}'"
            result = subprocess.run([command, options], check=True)

            # parse result
            match result:
                case 0:
                    # the server is accepting connections normally
                    isReady = True
                    message = 'The PostgreSQL server is accepting connections.'
                case 1:
                    # the server is rejecting connections
                    isReady = False
                    message = 'The PostgreSQL server is rejecting connections.'
                case 2:
                    # there was no response
                    isReady = False
                    message = 'The PostgreSQL server does not respond to connection attempts.'
                case 3:
                    # there was no attempt made, i.e. due to false connection parameters
                    isReady = True
                    message = 'The PostGreSQL could not be contacted.'

            # return dict
            return {'isHealthy': isReady, 'message': message}

        except FileNotFoundError:
            return {'isHealthy': False, 'message': 'The PostgreSQL client is not installed.'}

        except subprocess.CalledProcessError:
            return {'isHealthy': False, 'message': 'The PostgreSQL client is not installed.'}

        except Exception as e:
            raise RuntimeError(f'PostgreSQL Health Check - Error message: {e}')

    ####################################################################################################################
    # CONSTRUCTOR ######################################################################################################
    ####################################################################################################################
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super()
        return cls.__instance
