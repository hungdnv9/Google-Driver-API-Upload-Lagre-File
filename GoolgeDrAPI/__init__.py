from googleapiclient import discovery

from GoolgeDrAPI.myconfig import parents_id, log_file, timeout, keep
from GoolgeDrAPI.authorized import get_credential
from GoolgeDrAPI.folder import fd_create, fd_delete
from GoolgeDrAPI.file import upload
from GoolgeDrAPI.utils import rolling_delete, slack
import logging
import socket
import timeit

socket.setdefaulttimeout(timeout)


logger = logging.getLogger('GoolgeDrAPI')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

__author__ = "hungdnv"
creds = get_credential()
service = discovery.build('drive', 'v3', credentials=creds)


class InitApp:

    def exec(self):
        start = timeit.default_timer()
        # Create sub folder on base folder
        metadata_response = fd_create(service, parents_id=parents_id)
        # Upload into sub folder
        upload(service, parents_id=[metadata_response['id']])
        # Delele oldest file
        rolling_delete(service, keep)
        end = timeit.default_timer()
        seconds = end - start
        msg = f'Job finished at {seconds} seconds'
        logger.debug(msg)
        slack(msg)
