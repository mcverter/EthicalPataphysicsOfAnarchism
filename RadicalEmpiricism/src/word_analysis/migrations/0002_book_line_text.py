# Generated by Django 4.2.7 on 2023-12-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_line',
            name='text',
            field=models.TextField(null=True),
        ),
    ]