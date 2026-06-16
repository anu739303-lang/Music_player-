import os
import sys
from pathlib import Path

# Ensure Django project package parent is on sys.path
BASE_DIR = Path(__file__).resolve().parent
# The actual Django project package lives in the nested folder 'MusicPlayer/MusicPlayer'.
# Add the inner project parent (MusicPlayer) so `import MusicPlayer.settings` works.
sys.path.insert(0, str(BASE_DIR / "MusicPlayer"))

# Point to Django settings and expose WSGI application as `app` for Gunicorn
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MusicPlayer.settings")
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

if __name__ == "__main__":
	print("Music Player APP")