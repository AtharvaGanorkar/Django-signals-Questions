import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class AGModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=AGModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in this thread: {threading.get_ident()}")

def test_signal():
    print(f"Caller running in this thread: {threading.get_ident()}")
    AGModel.objects.create(name="Test")


test_signal()