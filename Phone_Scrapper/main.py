from scrapper import extract_phones
from export import save_to_file
from flask import Flask

save_to_file(extract_phones(3)) #10 pages
