#!/usr/bin/python

import sys
import zipCracker

print("""
 ______       _____ _ _       ____                _             
|__  (_)_ __ |  ___(_) | ___ / ___|_ __ __ _  ___| | _____ _ __ 
  / /| | '_ \| |_  | | |/ _ \ |   | '__/ _` |/ __| |/ / _ \ '__|
 / /_| | |_) |  _| | | |  __/ |___| | | (_| | (__|   <  __/ |   
/____|_| .__/|_|   |_|_|\___|\____|_|  \__,_|\___|_|\_\___|_|   
       |_|                                                     
""")

# Exit after the launch process exited
sys.exit(zipCracker.launch())
