import requests
import socket
import concurrent.futures
import requests
import speech_recognition as sr
from queue import Queue
from colored import fore, back, style
from bs4 import BeautifulSoup
import requests.exceptions
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
        domain = self.link

        def scan_subdomain(subdomain):
            domain = self.link
            """
            The regular expression pattern r"(https?://)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,63}\b)"
            is used to match and capture the different parts of the URL:
            (https?://): Matches the protocol (http:// or https://) and captures it in group 1.
            ([a-zA-Z0-9.-]+): Matches and captures the subdomain in group 2. It can consist of 
            letters, numbers, dots, and hyphens.
            (\.[a-zA-Z]{2,63}\b): Matches and captures the domain and top-level domain (TLD) in 
            group 3. It matches a dot followed by 2 to 63 letters.
            """
            pattern = r"(https?://)([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,63}\b)"
            """The re.sub function is then used to substitute the matched subdomain (\2) with 
            the desired string. The \1 and \3 references the captured protocol and domain parts, 
            respectively."""
            url = re.sub(pattern, r"\1" + subdomain + r"\2\3", domain)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Subdomain found: {url}")
                    with open("test_url.txt", "w") as file:
                        file.write(url + "\n")
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
