# Generated by Django 3.2.20 on 2023-07-19 06:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0097_alter_job_result_remove_result"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobresult",
            old_name="data",
            new_name="result",
        ),
    ]