# Generated by Django 3.2 on 2023-10-10 17:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0002_alter_lessonviesinfo_unique_together'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LessonViesInfo',
            new_name='LessonViewInfo',
        ),
    ]
