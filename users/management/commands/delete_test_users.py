from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Delete all test users except superusers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--emails',
            nargs='+',
            help='Specific emails to delete',
        )

    def handle(self, *args, **options):
        if options['emails']:
            User.objects.filter(email__in=options['emails']).delete()
            self.stdout.write(f"✅ Deleted users: {options['emails']}")
        else:
            count = User.objects.exclude(is_superuser=True).count()
            User.objects.exclude(is_superuser=True).delete()
            self.stdout.write(f"✅ Deleted {count} test users")