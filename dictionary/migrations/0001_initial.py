# Generated by Django 4.0.4 on 2023-01-23 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('shadow', models.IntegerField()),
                ('shadowColor', models.IntegerField()),
                ('border', models.IntegerField()),
                ('creators', models.TextField()),
                ('postNumber', models.IntegerField(null=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='행인', max_length=30)),
                ('consonant', models.CharField(max_length=10)),
                ('contents', models.TextField()),
                ('like', models.PositiveBigIntegerField(null=True)),
                ('stack', models.PositiveBigIntegerField(null=True)),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='dictionary.dictionary')),
            ],
        ),
    ]