# Generated by Django 2.2 on 2019-04-18 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qcontent', models.CharField(max_length=100)),
                ('qpub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acontent', models.CharField(max_length=100)),
                ('acount', models.IntegerField(max_length=100)),
                ('aquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.Questions')),
            ],
        ),
    ]
