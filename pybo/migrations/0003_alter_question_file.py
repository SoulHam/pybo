# Generated by Django 4.0.3 on 2022-12-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_question_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]