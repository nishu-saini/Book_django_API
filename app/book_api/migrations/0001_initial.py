# Generated by Django 4.2.6 on 2023-10-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number_of_pages', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
