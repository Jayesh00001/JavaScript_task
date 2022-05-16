from sys import api_version
from google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = '/home/vkaps-lp-101/Downloads/client_secret_file.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print(dir(service))