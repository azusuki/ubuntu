# Generated by Django 4.0.1 on 2022-02-28 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_check', models.BooleanField(default=False, verbose_name='表示フラグ')),
                ('title', models.CharField(max_length=100)),
                ('title_num', models.IntegerField()),
                ('foreign_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.area')),
            ],
        ),
    ]
