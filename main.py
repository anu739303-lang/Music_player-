import os
import sys
from pathlib import Path

# Ensure project root is on sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Point to Django settings and expose WSGI application as `app` for Gunicorn
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MusicPlayer.settings")
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

if __name__ == "__main__":
	print("Music Player APP")