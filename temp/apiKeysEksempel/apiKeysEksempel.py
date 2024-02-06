# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
# https://pypi.org/project/python-dotenv/

import os
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv('API_key')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')

print(API_key)