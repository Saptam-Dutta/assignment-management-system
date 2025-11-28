import datetime
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import os

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        log_dir = os.path.join(settings.BASE_DIR, "logs")
        os.makedirs(log_dir, exist_ok=True)

        logfile = os.path.join(log_dir, "requests.log")

        user = request.user.username if request.user.is_authenticated else "Anonymous"

        log_entry = f"[{datetime.datetime.now()}] {request.method} {request.path} - {user}\n"

        with open(logfile, "a") as f:
            f.write(log_entry)

        return None
