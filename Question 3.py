# models.py
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=100)

class Log(models.Model):
    message = models.CharField(max_length=255)

# Signal to create a log entry after a Book is saved
@receiver(post_save, sender=Book)
def log_book_save(sender, instance, **kwargs):
    print("Signal Triggered")
    Log.objects.create(message=f"Book '{instance.title}' was saved.")

# Code to simulate transaction and rollback
def create_book_with_exception():
    try:
        with transaction.atomic():
            # Create a new book
            book = Book.objects.create(title="New Book")
            # Signal will be triggered here and Log entry will be created

            # Simulate an error after signal has been triggered
            raise Exception("Simulated error after signal")
    except Exception as e:
        print(f"Exception caught: {e}")
