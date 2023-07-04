import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# FLASK_DEBUG = True
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# Redis cache
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT2')

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    # 'CACHE_REDIS_URL': 'redis://redis:6379/0',
    'CACHE_REDIS_URL': f'redis://{REDIS_HOST}:{REDIS_PORT}/0',
    'CACHE_DEFAULT_TIMEOUT': 60 * 60 * 24,  # 1 day default (in secs)
}

# Database connection
POSTGRES_HOST = os.environ.get('POSTGRES_HOST') 
POSTGRES_PORT = int(os.environ.get('DB_PORT3')) 
POSTGRES_DB = os.environ.get('POSTGRES_DB') 
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD =os.environ.get('POSTGRES_PASSWORD')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}'

# Superset metadata database (SQLite or other)
# METADATA_DB_URI = 'sqlite:////var/lib/superset/superset.db'

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.environ.get('SECRET_KEY')

# Flask-WTF flag for CSRF
# WTF_CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
# MAPBOX_API_KEY = os.environ.get('MAPBOX_API_KEY')

#---------------------------------------------------------
# Superset common config
#---------------------------------------------------------
# Specify the username for Superset to run as
SUPERSET_USERNAME = os.environ.get('SUPERSET_USER')

# Specify the password for Superset to use
SUPERSET_PASSWORD = os.environ.get('SUPERSET_PASSWORD')

# Whether to require users to log in to access Superset
# # AUTH_USER_REGISTRATION = False

# # Allow users to self-register
# AUTH_USER_REGISTRATION_ROLE = 'Public'

# # Enable SQLAlchemy event logging
# SQLALCHEMY_RECORD_QUERIES = False

#---------------------------------------------------------
# Extra configuration options for Superset
#---------------------------------------------------------
# Uncomment the following line to allow SQL Lab to execute queries in a separate process
#ENABLE_ASYNC_QUERIES = True

# Uncomment the following line to use AWS S3 for file uploads
#UPLOADED_FILE_DEST = '/path/to/s3/bucket'

# Uncomment the following lines to configure Superset to send emails
#EMAIL_NOTIFICATIONS = True
#SMTP_HOST = 'your_smtp_host'
#SMTP_PORT = 'your_smtp_port'
#SMTP_USERNAME = 'your_smtp_username'
#SMTP_PASSWORD = 'your_smtp_password'
#SMTP_STARTTLS = True
#SMTP_SSL = False
#SMTP_TLS = False
#SMTP_MAIL_FROM = 'your_email_address'

#---------------------------------------------------------
# Path to the data directory
# #---------------------------------------------------------
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATA_DIR = os.path.join(BASE_DIR, 'dataset')

# Enable superset to listen on all network interfaces
WEB_SERVER_ADDRESS = '0.0.0.0'
