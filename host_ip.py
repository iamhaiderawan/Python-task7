import socket

def show_host_ip():
    hostname = input("Please enter website URL : ")
    try:
        print(f'Hostname:{hostname}')
        print(f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print(f'Invalid Hostname, error: {error}')

show_host_ip()