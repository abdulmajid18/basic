import socket
from django.http import HttpResponse


def hello_world(request):
    # Get the hostname
    hostname = socket.gethostname()

    # Get the IP address
    ip_address = socket.gethostbyname(hostname)

    # Log the hostname and IP address
    print(f"Hostname: {hostname}, IP Address: {ip_address}")

    # Return the response
    return HttpResponse(f"VERSION 2: Hello from {hostname} ({ip_address})")
