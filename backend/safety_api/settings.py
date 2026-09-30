from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='dev-only-she-shield-key'
DEBUG=True
ALLOWED_HOSTS=['127.0.0.1','localhost']
INSTALLED_APPS=['django.contrib.contenttypes','django.contrib.auth','corsheaders','rest_framework','safety_api']
MIDDLEWARE=['corsheaders.middleware.CorsMiddleware','django.middleware.common.CommonMiddleware']
ROOT_URLCONF='safety_api.urls'
TEMPLATES=[]
WSGI_APPLICATION='safety_api.wsgi.application'
# Database intentionally omitted: this educational API is database-free.
DATABASES={}
CORS_ALLOW_ALL_ORIGINS=True
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
