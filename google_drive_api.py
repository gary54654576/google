from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import io

class GoogleDriveAPI:
    def __init__(self, credentials_file: str):
        self.credentials_file = credentials_file
        self.service = self._create_service()

    def _create_service(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file,
                scopes=["https://www.googleapis.com/auth/drive.readonly"]
            )
            return build("drive", "v3", credentials=credentials)
        except HttpError as error:
            print(f"An error occurred while creating Google Drive service: {error}")
            return None

    def get_file_by_id(self, file_id):
        try:
            request = self.service.files().get_media(fileId=file_id)
            file_content = io.BytesIO()
            downloader = MediaIoBaseDownload(file_content, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            file_content.seek(0)
            return file_content
        except HttpError as error:
            print(f"An error occurred while getting file by ID: {error}")
            return None
