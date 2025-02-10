from zipfile import ZipFile
from string import digits
import itertools

zip_filename = "1926.zip" # here the name of the rar file is '1926.zip'.
brute_force_attempts = itertools.product(digits, repeat=5) # all 5 digits possible.

with ZipFile(zip_filename) as zip_file:
    for attempt in brute_force_attempts:
        password = "ctflag" + "".join(attempt)

        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"[+] Password found: {password}")
            break 
        except:
            pass  
