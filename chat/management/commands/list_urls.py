from django.core.management.base import BaseCommand
from django.urls import get_resolver


class Command(BaseCommand):
    help = "List all registered URLs"

    def handle(self, *args, **kwargs):
        url_patterns = get_resolver().url_patterns
        for pattern in url_patterns:
            self.stdout.write(str(pattern))
