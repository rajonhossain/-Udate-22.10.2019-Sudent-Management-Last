# Generated by Django 2.2 on 2019-10-21 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0004_auto_20191021_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Type', models.CharField(choices=[('Admin', 'Admin'), ('Bangla', 'Bangla'), ('Student', 'Student')], default='student', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worktype', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='viewtype',
        ),
    ]
