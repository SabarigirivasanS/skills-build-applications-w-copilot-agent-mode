from django.db import migrations
from django.conf import settings

def create_email_unique_index(apps, schema_editor):
    from djongo.database import connect
    client = connect(settings.DATABASES['default']['NAME'])
    db = client[settings.DATABASES['default']['NAME']]
    db.users.create_index([('email', 1)], unique=True)

def drop_email_unique_index(apps, schema_editor):
    from djongo.database import connect
    client = connect(settings.DATABASES['default']['NAME'])
    db = client[settings.DATABASES['default']['NAME']]
    db.users.drop_index('email_1')

class Migration(migrations.Migration):
    dependencies = [
        ('octofit_tracker', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_email_unique_index, drop_email_unique_index),
    ]
