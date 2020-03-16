from datetime import datetime
import os 

# Set the log file. Default: /tmp/gg_driver_upload.log
log_file = '/tmp/upload-file-driver.log'

# Name of file
file_name = 'example.zip'

# mimetype of file
mimeType = 'application/zip'

# Path of file
file_path = '/tmp/'+ file_name

# Set the credentials file
credential_file = '/home/hungdnv/data/google-driver-data/credentials.json'

# Set the token file
token_file = '/home/hungdnv/data/google-driver-data/token.pickle'


# Base google driver folder id
parents_id= ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']

# Sub folder name
folder_name = 'folder_' + datetime.now().strftime('%Y%m%d_%H%M%S')

# Maximum retry upload
number_retry_upload = 3

# Set request timeout, unit is seconds
timeout = 30

# How many folder/days want to keep in Driver
keep = 7

# Track last folders created
last_folders_db_file = '/tmp/last_folders.db'

# Slack notification
slack_status = True
# change it on private acess
webhook_url = os.getenv('webhook_url')
channel_id = 'G6ECU42F7'

