import requests
import functools
import shutil
import codecs
import sys
import os
import tkinter as tk
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Create a tkinter main window
window = tk.Tk()
window.title("Web Page Data Extractor")

# Function to start the extraction when the user clicks the "Extract" button
def start_extraction():
    global url, use_tor_network
    url = url_entry.get()
    use_tor_network = tor_checkbox_var.get()
    extractor = Extractor(url)
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Extracting files from {url}\n\n")
    output_text.config(state=tk.DISABLED)
    extractor.run()
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, f"\nTotal extracted files: {len(extractor.scraped_urls)}")
    output_text.config(state=tk.DISABLED)

# URL of the web page you want to extract data from
url = ""

# Whether to use the Tor network
use_tor_network = False

# ... (rest of the code remains the same)

# Function to create the output folder
def create_output_folder():
    global output_folder
    output_folder = urlparse(url).netloc

# Initialize a session
session = requests.session()
if use_tor_network:
    session.request = functools.partial(session.request, timeout=30)
    session.proxies = {'http':  'socks5h://localhost:9050',
                        'https': 'socks5h://localhost:9050'}

# Define workspace from script location
workspace = os.path.dirname(os.path.realpath(__file__))

class Extractor:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_page_content(url), "html.parser")

        self.scraped_urls = self.scrap_all_urls()
    
    def run(self):
        self.save_files(self.scraped_urls)
        self.save_html()
    
    # ... (rest of the code remains the same)

# Create and pack widgets for the tkinter UI
url_label = tk.Label(window, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

tor_checkbox_var = tk.BooleanVar()
tor_checkbox = tk.Checkbutton(window, text="Use Tor Network", variable=tor_checkbox_var)
tor_checkbox.pack()

extract_button = tk.Button(window, text="Extract", command=start_extraction)
extract_button.pack()

output_text = tk.Text(window, width=60, height=15)
output_text.config(state=tk.DISABLED)
output_text.pack()

window.mainloop()
