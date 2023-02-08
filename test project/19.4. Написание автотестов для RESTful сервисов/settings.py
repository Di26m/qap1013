import os
from dotenv import load_dotenv

load_dotenv()


# valid_email = 'zzzzz@mail.ru'
# valid_password = 'zzzzz'

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')