from GoolgeDrAPI.myconfig import folder_name
from GoolgeDrAPI.utils import slack
import logging

logger = logging.getLogger('GoolgeDrAPI')

def fd_create(service, *args, **kargs):
    ''' Return a dict, key is folder name, and value is folder ID '''
    base_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'        
    }
    
    if 'parents_id' in kargs:
        base_metadata['parents'] = kargs['parents_id']
    msg = f'Create Folder, generate metadata {base_metadata}'
    logger.debug(msg)
    slack(msg)

    try:
        _object = service.files().create(body=base_metadata,
                                    fields='id').execute()
        metadata_response =  {
            'name': folder_name,
            'id': _object.get('id')
        }
        msg = f'Create folder success, detail {metadata_response}'
        logger.debug(msg)
        slack(msg)
    
    except Exception as err:
        msg = f'Create folder failed, reason {err}'
        logger.error(msg)
        slack(msg)

    return metadata_response

def fd_delete(service, *args, **kargs):    
    try:
        if args:
            for id in args:
                msg = f'Delete object {id}'
                logger.debug(msg)
                slack(msg)
                service.files().delete(fileId=id).execute()
        if 'folder_id' in kargs:
                msg = f'Delete object {kargs["folder_id"]}'
                logger.debug(msg)
                slack(msg)
                service.files().delete(fileId=kargs['folder_id']).execute()
    except Exception as err:
        msg = f'Delete failed, reason {err}'
        logger.error(msg)
        slack(msg)



 
