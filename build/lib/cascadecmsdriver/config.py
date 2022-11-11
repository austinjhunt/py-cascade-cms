import os
from dotenv import load_dotenv
from driver import CascadeCMSRestDriver
load_dotenv('../../.env')
CASCADE_API_KEY = os.environ.get('CASCADE_API_KEY')
CASCADE_ORG = os.environ.get('CASCADE_ORG')
CASCADE_USERNAME = os.environ.get('CASCADE_USERNAME')
CASCADE_PASSWORD = os.environ.get('CASCADE_PASSWORD')
driver = CascadeCMSRestDriver(
    organization_name=CASCADE_ORG, api_key=CASCADE_API_KEY)
