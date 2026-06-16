"""
Top-level WSGI shim for Render/Gunicorn.

This file exposes `application` as expected by `gunicorn MusicPlayer.wsgi:application`.
It delegates to the inner Django project's WSGI module at `MusicPlayer.MusicPlayer.wsgi`.
"""
try:
    # Import application from inner package
    from MusicPlayer.MusicPlayer.wsgi import application
except Exception:
    # Fallback: raise a clear error for debugging in logs
    raise
