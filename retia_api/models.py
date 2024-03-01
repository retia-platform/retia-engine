from django.db import models

class Device(models.Model):
    hostname=models.CharField(max_length=63, primary_key=True)
    mgmt_ipaddr=models.GenericIPAddressField()
    port=models.IntegerField(default=443)
    username=models.CharField(max_length=16, default=None)
    secret=models.CharField(max_length=64, default=None)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname

class Detector(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    device_interface_to_filebeat = models.CharField(max_length=200, default=None)
    device_interface_to_server=models.CharField(max_length=200, default=None)
    window_size = models.IntegerField(default=1)
    sampling_interval = models.IntegerField(default=20)
    elastic_host = models.CharField(max_length=200, default="127.0.0.1")
    elastic_index = models.CharField(max_length=255)
    filebeat_host = models.GenericIPAddressField()
    filebeat_port = models.IntegerField(default=50255)

    def __str__(self):
        return self.device.hostname

class ActivityLog(models.Model):
    time = models.DateTimeField(null=True)
    severity = models.CharField(max_length=255, blank=True)
    instance = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=10, blank=True)
    messages = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return "%s | %s | %s | %s | %s"%(self.time, self.severity, self.instance, self.category, self.messages)