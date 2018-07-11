FOLDER = '1J_Yw3ENBfDOEjiPV2LpYIa86aAPnaVx3'

import sys
if sys.version_info < (3, 3):
    sys.stderr.write("Sorry, requires at least Python 3.3\n")
    sys.exit(1)

import os
import pickle
import shlex
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

try:
    with open(os.path.expanduser('~/.local/share/drive-download/seen.pickle'), 'rb') as f:
        seen = pickle.load(f)
except FileNotFoundError:
    seen = set()

gauth = GoogleAuth(settings_file=os.path.expanduser('~/.config/drive-download/settings.yaml'))
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(FOLDER)}).GetList()
for file1 in file_list:
    if file1['mimeType'] == 'application/vnd.google-apps.folder':
        continue
    if file1['id'] in seen:
        continue

    local_filename = file1['title']
    print(shlex.quote(local_filename))
    if not os.path.exists(local_filename):
        file1.GetContentFile(local_filename)
        seen.add(file1['id'])
        with open(os.path.expanduser('~/.local/share/drive-download/seen.pickle'), 'wb') as f:
            pickle.dump(seen, f)
    else:
        raise RuntimeError("{} exists".format(shlex.quote(local_filename)))
