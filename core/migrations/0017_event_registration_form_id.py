import re
from urllib.parse import urlsplit

from django.db import migrations, models
from django.core.validators import RegexValidator


def extract_google_form_ids(apps, schema_editor):
    Event = apps.get_model('core', 'Event')
    database = schema_editor.connection.alias

    for event in Event.objects.using(database).exclude(registration_link__isnull=True).exclude(registration_link='').iterator():
        parts = urlsplit(event.registration_link)
        if parts.hostname != 'docs.google.com':
            continue

        match = re.fullmatch(r'/forms/(?:d/e/|d/)([^/]+)/(?:viewform|edit)', parts.path)
        if match:
            event.registration_link = match.group(1)
            event.save(using=database, update_fields=['registration_link'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_event_short_description'),
    ]

    operations = [
        migrations.RunPython(extract_google_form_ids, migrations.RunPython.noop),
        migrations.RenameField(
            model_name='event',
            old_name='registration_link',
            new_name='registration_form_id',
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_form_id',
            field=models.CharField(
                blank=True,
                help_text='Masukkan ID saja, bukan URL. Contoh: 1FAIpQL...',
                max_length=255,
                null=True,
                validators=[
                    RegexValidator(
                        regex='^[A-Za-z0-9_-]+$',
                        message='Masukkan ID Google Form saja, bukan URL.',
                    ),
                ],
                verbose_name='Google Form ID',
            ),
        ),
    ]
