# Open FDA
This is a crazy simple script that pulls data from the open FDA API and writes it to a csv. 

### Installation
Ensure that you're in a preferred python dev environment with pip installed, and run `pip install -r requirements.txt`

### Usage
2 usages:
1. To pull from the openFDA API, run `python3 fda.py` from the root directory. Ensure `python >=3.8` Script will start and write a `filename.csv` locally, so ensure that system has >= 100mb of memory. 

2. To convert all 510(k) data from the openFDA, first download the full JSON package and unpack, then run `python3 fda_simple.py`

