# Cisco Meraki switch port configuration
- Script was made in Python 3.7 and requires requests module.
### Overview
-	Purpose was to take advantage of swapping out Cisco switches and reorganize the dreaded spaghetti cables found inside the server room, that makes cable tracing troublesome and overall neatness unsupportable.
-	Project consists of two Python scripts:
    - **Meraki_port_backup.py** which creates two files of all port configurations of a given Meraki switch into a json file. 
      - A *Restore* file for restoration purposes that should not be touched.
      - An *Update* file in which you can update all necessary ports configurations to start organizing patch cables.
    - **Meraki_port_update.py** which automates updates reading the updated file of port configurations and outputs the status of each update being made.
### Requirements
- Meraki APIs have to be enabled on your dashboard in order to obtain an API Key.
- Python has to be installed.
  - After Python is installed the requests module also must be installed.
    - pip install requests

