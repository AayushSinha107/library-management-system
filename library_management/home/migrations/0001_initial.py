# Generated by Django 4.1.2 on 2022-11-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_code', models.CharField(max_length=7)),
                ('book_name', models.CharField(max_length=30)),
                ('book_author', models.CharField(max_length=60, null=True)),
                ('book_added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]