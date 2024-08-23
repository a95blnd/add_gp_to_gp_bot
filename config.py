import os

admins = [895067189]  # admins user ids
token = os.getenv("TOKEN", "")

host_db = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_NAME", "")
user_db = os.getenv("DB_USER", "")
passwd_db = os.getenv("DB_PASS", "")
port = int(os.getenv("DB_PORT", 3306))

python_version = os.getenv("PYTHON_VERSION", "python3")