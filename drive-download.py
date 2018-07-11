FOLDER = '1J_Yw3ENBfDOEjiPV2LpYIa86aAPnaVx3'

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(FOLDER)}).GetList()
for file1 in file_list:
    if file1['mimeType'] == 'application/vnd.google-apps.folder':
        continue
    local_filename = file1['title']
    print(local_filename)
    if not os.path.exists(local_filename):
        file1.GetContentFile(local_filename)
    else:
        raise "{} exists".format(local_filename)
