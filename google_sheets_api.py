from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GoogleSheetsAPI:
    def __init__(self, credentials_file: str, spreadsheet_id: str):
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.service = self._create_service()

    def _create_service(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file,
                scopes=["https://www.googleapis.com/auth/spreadsheets"]
            )
            return build("sheets", "v4", credentials=credentials)
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def get_user_data(self):
        DATA_RANGE = 'user data!A2:E'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            user_data = result.get('values', [])
            return user_data
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_languages(self):
        DATA_RANGE = 'languages!B2:B'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            languages = result.get('values', [])
            return [language[0] for language in languages]
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_messages(self):
        DATA_RANGE = 'messages!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            messages = result.get('values', [])
            return messages
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_menu_categories(self):
        DATA_RANGE = 'menu buttons!A2:A'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            categories = result.get('values', [])
            return [category[0] for category in categories]
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_common_data(self):
        DATA_RANGE = 'common!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            common_data = result.get('values', [])
            return common_data
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_common_images(self):
        IMAGES_RANGE = 'common!C2:C'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=IMAGES_RANGE).execute()
            common_images = result.get('values', [])
            return common_images
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []


    def get_titles(self):
        DATA_RANGE = 'titles!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            titles = result.get('values', [])
            return titles
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_descriptions(self):
        DATA_RANGE = 'descriptions!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            descriptions = result.get('values', [])
            return descriptions
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_menu_category_button_names(self):
        DATA_RANGE = 'menu buttons!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            buttons = result.get('values', [])
            return buttons
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def get_button_names_by_action(self):
        DATA_RANGE = 'action buttons!A2:D'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            buttons = result.get('values', [])
            return buttons
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def load_data_from_google_sheets(self):
        DATA_RANGE = 'user data!A2:E'
        try:
            result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=DATA_RANGE).execute()
            user_data = result.get('values', [])
            return user_data
        except HttpError as error:
            print(f"An error occurred: {error}")
            return []

    def update_user_data(self, user_info):
        id = user_info[0]
        row = self.get_user_row_by_id(id)

        body = {
            'values': [
                [user_info[0], user_info[1], user_info[2], user_info[3], user_info[4]]
            ]
        }

        try:
            # Check if the user already exists
            if id in [row[0] for row in self.load_data_from_google_sheets()]:
                result = self.service.spreadsheets().values().update(
                    spreadsheetId=self.spreadsheet_id,
                    range=f'user data!A{row}:E{row}',
                    valueInputOption='RAW',
                    body=body
                ).execute()
            else:
                # If the user does not exist, append the new data
                result = self.service.spreadsheets().values().append(
                    spreadsheetId=self.spreadsheet_id,
                    range=f'user data!A:E',
                    valueInputOption='RAW',
                    body=body
                ).execute()
            print(f"Updated user data: {result}")
        except HttpError as error:
            print(f"An error occurred: {error}")

    def get_user_row_by_id(self, id):
        data = self.load_data_from_google_sheets()
        col_values = [row[0] for row in data]
        if id in col_values:
            return col_values.index(id) + 2
        return len(col_values) + 2
