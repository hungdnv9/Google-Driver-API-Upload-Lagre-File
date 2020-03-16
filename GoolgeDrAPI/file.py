from apiclient.http import MediaFileUpload
from GoolgeDrAPI.myconfig import file_name, file_path, mimeType, number_retry_upload
from GoolgeDrAPI.utils import slack
import os 
import sys
import logging
import time

logger = logging.getLogger('GoolgeDrAPI')

def upload(service, *args, **kargs):

    if not os.path.exists(file_path):
        msg = f'File not found {file_path}'
        logger.debug(msg)
        slack(msg)        
        sys.exit()
    else:
        msg = f'Upload file, src_file {file_path}, size {os.path.getsize(file_path)} bytes'
        logger.debug(msg)
        slack(msg) 
        base_metadata = {
            'name': file_name,            
            'mimeType': mimeType
        }
        if 'parents_id' in kargs:
            base_metadata['parents'] = kargs['parents_id']
        
        msg = f'File metadata {base_metadata}'
        logger.debug(msg)
        slack(msg)

        base_payload =  MediaFileUpload(file_path, chunksize=1024*1024, resumable = True)
        request = service.files().create(body=base_metadata,media_body=base_payload)

        upload_sucess = "No"
        upload_failed_count = 0
        while upload_sucess == "No":
            try:                             
                response = None
                while response is None:

                    status, response = request.next_chunk()
                    if status:
                        logger.debug(f"Upload progress {int(100*status.progress())}%")
                    else:
                        msg = f'Uploaded done, detail {response}'                        
                        logger.debug(msg)
                        slack(msg)
                
                upload_sucess = 'Yes'

            except Exception as err:
                msg = f'Upload error, detail {err}'
                logger.debug(msg)
                slack(msg)

                upload_sucess = "No"
                upload_failed_count += 1

                msg = f'Try upload again, try count {upload_failed_count}'
                logger.debug(msg)
                slack(msg)

                time.sleep(5)        
                if upload_failed_count == number_retry_upload:
                    msg = "Maximum number of retry upload, Stop upload job"
                    logger.debug(msg)
                    slack(msg)
                    sys.exit()
