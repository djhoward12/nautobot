# Generated by Django 4.2.16 on 2024-11-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wireless", "0001_initial"),
        ("dcim", "0065_controller_capabilities_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="controllermanageddevicegroup",
            name="radio_profiles",
            field=models.ManyToManyField(
                blank=True,
                related_name="controller_managed_device_groups",
                through="wireless.ControllerManagedDeviceGroupRadioProfileAssignment",
                to="wireless.radioprofile",
            ),
        ),
        migrations.AddField(
            model_name="controllermanageddevicegroup",
            name="wireless_networks",
            field=models.ManyToManyField(
                blank=True,
                related_name="controller_managed_device_groups",
                through="wireless.ControllerManagedDeviceGroupWirelessNetworkAssignment",
                to="wireless.wirelessnetwork",
            ),
        ),
    ]
