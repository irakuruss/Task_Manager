# Generated by Django 5.0.6 on 2024-06-23 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('statuses', '0002_alter_status_name'),
        ('tasks', '0003_alter_task_description_tasklabelrelation_task_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.TaskLabelRelation', to='labels.label', verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='statuses.status', verbose_name='Status'),
        ),
    ]