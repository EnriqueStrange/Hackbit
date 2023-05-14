import requests
import socket
import concurrent.futures
import requests
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import threading
from queue import Queue
from colored import fore, back, style
from bs4 import BeautifulSoup
import requests.exceptions
import urllib.parse
from collections import deque
import re
import paramiko
import sys
import os
import termcolor
import threading
import time
from IPy import IP
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


class LinkProcessor:
    def __init__(self):
        self.link = None

    def get_link_from_user(self):
        self.link = input("Enter a link: ")

    def process_link(self):
        if self.link is not None:
            response = requests.get(self.link)
            # process the response here
            print(response.status_code)
        else:
            print("No link was provided")

    def get_ip_address(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"Your system IP is {ip_address}")

    def subdomain_scanner(self):
        subdomain = self.link

        def scan_subdomain(subdomain):
            url = f"http://{subdomain}.example.com"  # Replace with your target domain
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Subdomain found: {subdomain}")
            except requests.ConnectionError:
                pass

        with open("subdomains.txt") as file:  # Replace with your list of subdomains
            subdomains = file.read().splitlines()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(scan_subdomain, subdomains)


if __name__ == "__main__":
    pentest = LinkProcessor()
    pentest.get_link_from_user()
    pentest.process_link()
    pentest.get_ip_address()
    pentest.subdomain_scanner()
