# Generated by Django 3.2 on 2022-08-01 23:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('references', '0002_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='groups',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='student_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
