# Question 2: Do Django signals run in the same thread as the caller?
# Answer:
# Yes, by default, Django signals run in the same thread as the caller.

# Code Example:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import threading
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received for:", instance.name)
    time.sleep(2)  # Simulate delay
    print("Signal handler finished")

# Creating an instance of MyModel
obj = MyModel.objects.create(name="Test")
print("Object created")
print("Current thread ID:", threading.get_ident())