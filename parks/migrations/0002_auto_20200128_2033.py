# Generated by Django 3.0.2 on 2020-01-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='park',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parks', to='parks.Park'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
