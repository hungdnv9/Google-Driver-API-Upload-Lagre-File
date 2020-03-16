from GoolgeDrAPI.myconfig import last_folders_db_file, parents_id, slack_status, webhook_url, channel_id
from GoolgeDrAPI.folder import fd_delete
import logging
from datetime import datetime
import requests
import json
logger = logging.getLogger('GoolgeDrAPI')

def list_object(service, pagesize):
    ''' Note that last object by default sorted by last create '''
    last_object = []
    results = service.files().list(q=f"'{parents_id[0]}' in parents and trashed = False",
        pageSize=pagesize, fields="nextPageToken, files(id, name, parents)").execute()
    items = results.get('files', [])
    msg = f'List last {pagesize-1} object in base folder {parents_id[0]}'
    logger.debug(msg)
    slack(msg)
    for item in items:
        logger.debug(item)
        slack(item)
        last_object.append(item)

    return last_object
        

def rolling_delete(service, limit=5):   
    oldest_object = list_object(service, limit+1)[-1]
    msg = f'Object will be delete {oldest_object["name"]} - {oldest_object["id"]}'
    logger.debug(msg)
    slack(msg)      
    fd_delete(service, folder_id=oldest_object["id"])


def slack(msg):

    if slack_status is False:
        # Disable post message to slack
        pass
    else:
        timestamp = datetime.now().strftime("%d/%m/%y %H:%M:%S")
        data = {
            "text": f"[{timestamp}] {msg}",
            "icon_emoji": ":ghost:",
            "username": "notification",
            "channel": channel_id
        }
        try:
            response = requests.post(url=webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            logger.debug(f'Post to Slack done, response code {str(response)}')            
        except Exception as err:
            logger.debug(f'Unable post requests to Slack, reason {err}')


