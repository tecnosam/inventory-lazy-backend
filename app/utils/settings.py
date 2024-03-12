import os

from dotenv import load_dotenv


load_dotenv()



ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')


JWT_SECRET = os.getenv('JWT_SECRET', 'secret')
JWT_ALGOL = os.getenv('JWT_ALGOL', 'HS256')

DATABASE_URI = os.getenv('DATABASE_URI')

