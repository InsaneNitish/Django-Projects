# Generated by Django 4.2.5 on 2023-10-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
            ],
        ),
    ]
