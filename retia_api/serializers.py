from rest_framework import serializers
from .models import Device, Detector, ActivityLog

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields=['hostname','mgmt_ipaddr', 'port', 'username', 'secret', 'created_at', 'modified_at']

class DetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Detector
        fields=["device", "device_interface_to_filebeat", "device_interface_to_server", "window_size", "sampling_interval", "elastic_host", "elastic_index","filebeat_host", "filebeat_port"]


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityLog
        fields=["time","severity","instance","category","messages"]