# Generated by Django 4.2.1 on 2023-06-04 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroup', '0003_study_author_study_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='tag',
            field=models.CharField(default='모집 중', max_length=10),
        ),
    ]