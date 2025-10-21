import os
import socket
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def detect_environment() -> str:
    """Return one of: local, dev, prod."""
    env = os.getenv("DJANGO_ENV")
    if env:
        return env.lower()

    # Docker hint
    if os.path.exists("/.dockerenv"):
        return "dev"

    # Hostname heuristics
    hostname = socket.gethostname().lower()
    if any(k in hostname for k in ("dev", "staging")):
        return "dev"
    if any(k in hostname for k in ("prod", "server")):
        return "prod"

    # Local marker
    if (BASE_DIR / ".env.local").exists():
        return "local"

    return "local"


DJANGO_ENV = detect_environment()
print(f"[settings] Loaded environment: {DJANGO_ENV}")

if DJANGO_ENV == "local":
    from .local import *
elif DJANGO_ENV == "dev":
    from .dev import *
elif DJANGO_ENV == "prod":
    from .prod import *
else:
    raise RuntimeError(f"Unknown environment: {DJANGO_ENV}")
