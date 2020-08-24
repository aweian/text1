from rest_framework import serializers
from .models import Device, Password


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "device_name",
            "device_mgmt_ip",
            "device_type",
            "os_version",
            # "device_brand_model",
            # "device_mode",
            # "networking_mode",
            # "cluster_status",
            # "status",
            # "device_area",
            # "is_hide",
            # "placement",
            # "device_capability",
            # "description",
            # "is_delete",
            # "is_nanotube",
            # "organization",
            "device_esn",
            # "device_assets",
            # "create_time",
            # "update_time",
        ]


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = [
            "id",
            "username",
            "password",
            "device",
            "connect_way",
            "port",
            "timeout",
            "type",
            "remark",
            "create_time",
            "update_time",
        ]
