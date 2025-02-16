from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler: Creating another MyModel instance...")
    MyModel.objects.create(name="Signal-created instance")


def test_signal():
    try:
        with transaction.atomic():
            print("Caller: Creating MyModel instance...")
            MyModel.objects.create(name="Caller-created instance")
            raise Exception("Forcing a rollback")
    except Exception as e:
       print(f"Exception caught: {e}")

test_signal()

for obj in MyModel.objects.all():
    print(f"ID: {obj.id}, Name: {obj.name}")