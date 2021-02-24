# Generated by Django 3.1.6 on 2021-02-14 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210212_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Semester',
            field=models.CharField(choices=[('א', 'א'), ('ב', 'ב'), ('ק', 'ק')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='api.course_group'),
        ),
    ]
