# Generated by Django 3.2.25 on 2024-07-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('due_date', models.DateTimeField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
    ]
