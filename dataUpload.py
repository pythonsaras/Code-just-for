from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os

# Authentication
gauth=GoogleAuth()
# Create local webserver and auto
# handles Authentication
gauth.LocalWebserverAuth()
drive=GoogleDrive(gauth)

path=r"F:\\Eduction"
for x in os.listdir(path):
    f=drive.CreateFile({'title':x})
    f.SetContentFile(os.path.join(path,x))
    f.Upload()
    f=None
