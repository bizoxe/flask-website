from pathlib import Path

from dotenv import load_dotenv

root_dir = Path(__file__).absolute().parent
env_file = root_dir / "src" / ".env"

load_dotenv(env_file)

# Worker Settings
workers = 4
worker_class = "gevent"
worker_connections = 1000

# Server Settings
bind = "0.0.0.0:8000"

# Timeout Settings
timeout = 30
graceful_timeout = 30

# Keep-Alive Settings
keepalive = 2

max_requests = 1000
max_requests_jitter = 50

# Logging Settings
accesslog = "-"
access_log_format = '%(h)s %(t)s "%(r)s" %(s)s %(b)s'
errorlog = "-"
loglevel = "error"
