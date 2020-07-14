import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for the database')
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable. Waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database is available!'))
