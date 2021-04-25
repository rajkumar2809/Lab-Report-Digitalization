# Generated by Django 2.0.5 on 2020-02-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]