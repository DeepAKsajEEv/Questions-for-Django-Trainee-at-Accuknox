import threading
from django.core.signals import Signal
from django.dispatch import receiver

# Define a custom signal
my_signal = Signal()

# Define the signal handler
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Handler thread ID: {threading.get_ident()}")

def emit_signal():
    print(f"Caller thread ID: {threading.get_ident()}")
    # Emit the signal
    my_signal.send(sender=None)

# Somewhere in your Django view or function
def some_view_or_function(request):
    # Emit signal inside the view or function
    emit_signal()
    return HttpResponse("Signal emitted and handled")
