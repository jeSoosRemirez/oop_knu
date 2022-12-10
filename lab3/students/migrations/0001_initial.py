# Generated by Django 2.2.24 on 2021-08-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='First name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last name')),
                ('middle_name', models.CharField(default='', max_length=256, verbose_name='First name')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo')),
                ('ticket', models.CharField(max_length=256, verbose_name='Ticket')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
            ],
        ),
    ]