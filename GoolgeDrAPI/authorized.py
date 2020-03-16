from httplib2 import Http
import httplib2
from oauth2client import file, client, tools
from apiclient import errors
from apiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os 
import sys
from GoolgeDrAPI.myconfig import credential_file, token_file
import logging
from GoolgeDrAPI.utils import slack

logger = logging.getLogger('GoolgeDrAPI')

def get_credential():
    creds = None
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            msg = f'Loading token ... from {token_file}'
            logger.debug(msg)
            slack(msg)
            creds = pickle.load(token)
            msg= 'Token load done !'
            logger.debug(msg)
            slack(msg)
    else:
        msg = f'File not found {token_file}'
        logger.debug(msg)
        slack(msg)
        sys.exit()
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            msg = 'Token expired, refresh token ...'
            logger.debug(msg)
            slack(msg)
            creds.refresh(Request())
            msg = 'Refresh token done !'
            logger.debug(msg)
            slack(msg)
        else:
            if not os.path.exists(credential_file):
                msg = f'File not found {credential_file}'
                logger.debug(msg)
                slack(msg)
                sys.exit()
            else:
                msg = 'Initialing token'
                logger.debug(msg)
                flow = InstalledAppFlow.from_client_secrets_file(credential_file, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, 'wb') as token:           
            pickle.dump(creds, token)
    msg = f'Authorized {creds}'
    logger.debug(msg)
    slack(msg)
    return creds
