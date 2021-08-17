import dropbox
import os
from posixpath import relpath
from dropbox.files import WriteMode

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(filename,root)

                relative_path = os.path.relpath(file_from,local_path)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A2v3hZtS1sFd7WoGFh3ykiGylQNaGCnec7XkhiLEb7_E1TUWZzTReYW_KWNGY9_FJCXf91wvi2iDdsZQ7CVZ2LIQqOPg6ObMcKXUun-ugRCsAwgwKImwTSNvq2Fr3Nwr42VgI9c'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/Rajjo/OneDrive/Desktop/test2.txt'
    file_to = '/SavingToDBX/test2.txt'

    transferData.upload_file(file_from,file_to)
    print("Successfully moved file")

main()
