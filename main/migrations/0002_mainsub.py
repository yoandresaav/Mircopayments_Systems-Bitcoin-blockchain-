# Generated by Django 2.2.5 on 2020-05-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.TextField()),
                ('name', models.TextField()),
                ('proof_of_work', models.TextField()),
                ('documentation', models.TextField()),
                ('charges_rules', models.TextField()),
            ],
        ),
    ]