import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Define a signal receiver
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal received!")
    # Introduce a delay to simulate a time-consuming operation
    time.sleep(5)  # Sleep for 5 seconds
    print("Signal handler finished!")

# Simulate saving a user instance
def create_user():
    print("Saving user...")
    user = User.objects.create(username='testuser')
    print("User saved!")

if __name__ == "__main__":
    create_user()
