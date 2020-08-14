import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Check the existing database connection"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Connecting database...'))

        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:

                self.stdout.write(self.style.ERROR('Database unavailable!!!'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!!!'))
