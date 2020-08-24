from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Device, Password
from .serializers import DeviceSerializer, PasswordSerializer
from rest_framework.response import Response
from rest_framework import status, generics
import django_filters.rest_framework
from pyexcel_xlsx import get_data


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.filter(is_delete=False)
    serializer_class = DeviceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [
            "id",
            "device_name",
            "device_mgmt_ip",
            "device_type",
            "os_version",
            "device_brand_model",
            "device_mode",
            "networking_mode",
            "cluster_status",
            "status",
            "device_area",
            "is_hide",
            "placement",
            "device_capability",
            "description",
            "is_delete",
            "is_nanotube",
            # "organization_id",
            "device_esn",
            "device_assets",
            "create_time",
            "update_time",
        ]

    def destroy(self, request, *args, **kwargs):
        # 逻辑删除
        device = self.get_object()
        device.is_delete = True
        device.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PasswordViewSet(ModelViewSet):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    filterset_fields = [
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

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DeviceFileViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        file_name = request.data["file"]
        data = get_data(file_name)
        serializer_list = []
        for sheet_name in data:
            sheet = data[sheet_name]
            field_name_list = sheet[0]
            filed_list = ["device_name", "device_mgmt_ip", "device_type", "OS_version", "device_brand_model", "device_mode", "networking_mode", "status", "device_area", "is_hide", "placement", "device_capability", "description", "device_esn", "device_assets",]

            for device_list in sheet[1::]:
                device = dict(zip(filed_list, device_list[1::]))
                device["is_hide"] = bool(int(device["is_hide"]))
                serializer = self.get_serializer(data=device)
                serializer.is_valid(raise_exception=True)
                serializer_list.append(serializer)
        for serializer in serializer_list:
            serializer.save()
        return Response("serializer.data 测试成功", status=status.HTTP_201_CREATED, headers={'Location': "导入成功"})











