# Upload Compress File Daily To Google Driver via Google Driver APIv3

# Features
- Logging and console 
- Rolling detele old file on driver
- Sub folder struct, separating by datetime prefix
- Intergrate with notification to Slack
- Supported upload large file. Note that currently, i just make it support only one mimetype 'application/zip' to apply my task. For more futher, you can refer to the Google Driver API documet page.

# Requre and install
- Python ^3.6
- Install: pip install -r requirements.txt
- Also please change the config in 'myconfig.py'

# Example console and log output
```shell
$ python run.py 
2020-03-16 17:31:04,942 - GoolgeDrAPI - DEBUG - Loading token ... from /home/hungdnv/data/google-driver-data/token.pickle
2020-03-16 17:31:04,942 - GoolgeDrAPI - DEBUG - Token load done !
2020-03-16 17:31:04,942 - GoolgeDrAPI - DEBUG - Authorized <google.oauth2.credentials.Credentials object at 0x7fc671523950>
2020-03-16 17:31:05,237 - GoolgeDrAPI - DEBUG - Create Folder, generate metadata {'name': 'folder_20200316_173104', 'mimeType': 'application/vnd.google-apps.folder', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:06,417 - GoolgeDrAPI - DEBUG - Create folder success, detail {'name': 'folder_20200316_173104', 'id': '1ReyG1G8D1KbFkqDbwn49ugUS6jnoq4wI'}
2020-03-16 17:31:06,417 - GoolgeDrAPI - DEBUG - Upload file, src_file /tmp/example.zip, size 20971520 bytes
2020-03-16 17:31:06,418 - GoolgeDrAPI - DEBUG - File metadata {'name': 'example.zip', 'mimeType': 'application/zip', 'parents': ['1ReyG1G8D1KbFkqDbwn49ugUS6jnoq4wI']}
2020-03-16 17:31:07,461 - GoolgeDrAPI - DEBUG - Upload progress 5%
2020-03-16 17:31:07,848 - GoolgeDrAPI - DEBUG - Upload progress 10%
2020-03-16 17:31:08,254 - GoolgeDrAPI - DEBUG - Upload progress 15%
2020-03-16 17:31:08,600 - GoolgeDrAPI - DEBUG - Upload progress 20%
2020-03-16 17:31:08,915 - GoolgeDrAPI - DEBUG - Upload progress 25%
2020-03-16 17:31:09,310 - GoolgeDrAPI - DEBUG - Upload progress 30%
2020-03-16 17:31:09,696 - GoolgeDrAPI - DEBUG - Upload progress 35%
2020-03-16 17:31:10,046 - GoolgeDrAPI - DEBUG - Upload progress 40%
2020-03-16 17:31:10,465 - GoolgeDrAPI - DEBUG - Upload progress 45%
2020-03-16 17:31:10,885 - GoolgeDrAPI - DEBUG - Upload progress 50%
2020-03-16 17:31:11,244 - GoolgeDrAPI - DEBUG - Upload progress 55%
2020-03-16 17:31:11,694 - GoolgeDrAPI - DEBUG - Upload progress 60%
2020-03-16 17:31:12,107 - GoolgeDrAPI - DEBUG - Upload progress 65%
2020-03-16 17:31:12,477 - GoolgeDrAPI - DEBUG - Upload progress 70%
2020-03-16 17:31:12,956 - GoolgeDrAPI - DEBUG - Upload progress 75%
2020-03-16 17:31:13,390 - GoolgeDrAPI - DEBUG - Upload progress 80%
2020-03-16 17:31:13,842 - GoolgeDrAPI - DEBUG - Upload progress 85%
2020-03-16 17:31:14,193 - GoolgeDrAPI - DEBUG - Upload progress 90%
2020-03-16 17:31:14,524 - GoolgeDrAPI - DEBUG - Upload progress 95%
2020-03-16 17:31:16,175 - GoolgeDrAPI - DEBUG - Uploaded done, detail {'kind': 'drive#file', 'id': '1W2MwKp8JKGTiIPi6HytHuYj38UNuUdHx', 'name': 'example.zip', 'mimeType': 'application/zip'}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - List last 7 object in base folder 1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1ReyG1G8D1KbFkqDbwn49ugUS6jnoq4wI', 'name': 'folder_20200316_173104', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1GrIWY9wQe7iy2Y4WirZdmGtsWCmiwBBk', 'name': 'folder_20200316_172604', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1FYzxxm1ey_Zo0q_2Pz8dl0EiGYIbe5BN', 'name': 'folder_20200316_172423', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1JQQkc8c1lYETg9MpYTg_kzXb1U9b5VKX', 'name': 'folder_20200316_172328', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1S9D5pn7U2un8K0Y8IV7O2QD_1_-elD1I', 'name': 'folder_20200316_172038', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1oaH0AgexCRyj7TMbVTnBigpQFlMRwgpU', 'name': 'folder_20200316_172012', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1M3KQm5K8mWVaRkg_7LMePoKeM1tNMC50', 'name': 'folder_20200316_171904', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,748 - GoolgeDrAPI - DEBUG - {'id': '1VRGe-f7jFxWnSgPIxRLozU55SIJz7sBc', 'name': '20200316_17', 'parents': ['1w1A0gC3Qe9uH37QSFi0e0MDY__jqNE8l']}
2020-03-16 17:31:16,749 - GoolgeDrAPI - DEBUG - Object will be delete 20200316_17 - 1VRGe-f7jFxWnSgPIxRLozU55SIJz7sBc
2020-03-16 17:31:16,749 - GoolgeDrAPI - DEBUG - Delete object 1VRGe-f7jFxWnSgPIxRLozU55SIJz7sBc
```

# Slack channel

![alt text](https://github.com/hungdnv9/Google-Driver-API-Upload-Lagre-File/blob/master/images/slack_notification.png)

# Google Driver

![alt text](https://github.com/hungdnv9/Google-Driver-API-Upload-Lagre-File/blob/master/images/drive_folder_struct.png) 

