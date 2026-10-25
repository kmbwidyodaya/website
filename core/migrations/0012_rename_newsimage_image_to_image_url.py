from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_media_embed_url_newsimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsimage',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image_url',
            field=models.URLField(
                help_text='Masukkan link gambar tambahan',
                verbose_name='Image URL',
            ),
        ),
    ]
