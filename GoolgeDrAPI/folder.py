from GoolgeDrAPI.myconfig import folder_name
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
        
    logger.debug(f'Create Folder, generate metadata {base_metadata}')

    try:
        _object = service.files().create(body=base_metadata,
                                    fields='id').execute()
        metadata_response =  {
            'name': folder_name,
            'id': _object.get('id')
        }
        logger.debug(f'Create folder success, detail {metadata_response}')
    
    except Exception as err:
        logger.error(f'Create folder failed, reason {err}')

    return metadata_response

def fd_delete(service, *args, **kargs):    
    try:
        if args:
            for id in args:
                logger.debug(f'Delete object {id}')
                service.files().delete(fileId=id).execute()
        if 'folder_id' in kargs:
                logger.debug(f'Delete object {kargs["folder_id"]}')
                service.files().delete(fileId=kargs['folder_id']).execute()
    except Exception as err:
        logger.error(f'Delete failed, reason {err}')



 
