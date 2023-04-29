import csv
import json
from typing import List, Dict
from datetime import datetime

def read_encodes_csv(file_path: str) -> Dict[str, str]:
    """Read the encodes.csv file and return a dictionary with hash as the key and long_url as the value."""
    encodes = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            encodes[f'http://{row["domain"]}/{row["hash"]}'] = row['long_url']
    return encodes

def read_decodes_json(file_path: str) -> List[Dict[str, str]]:
    """Read the decodes.json file and return a list of dictionaries containing decode data."""
    with open(file_path, 'r') as json_file:
        decodes = json.load(json_file)
    return decodes

def filter_decodes_by_year(decodes: List[Dict[str, str]], year: int) -> List[Dict[str, str]]:
    """
    Filter the decodes by the given year and return a list of 
    dictionaries containing decode data for the specified year.
    """
    filtered_result = []
    for decode in decodes:
        if datetime.fromisoformat(decode['timestamp']).year == year:
            filtered_result.append(decode)
        
    return filtered_result

def calculate_clicks(encodes: Dict[str, str], decodes: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Calculate the number of clicks for each long URL in the 
    encodes dictionary using the provided decodes data.
    Convert data to correct format:
    Example format: [{"https://google.com": 3}, {"https://www.twitter.com" : 2}]
    """
    clicks_data = {}
    for decode in decodes:
        bitlink = decode['bitlink']
        if decode['bitlink'] in encodes:
            long_url = encodes[bitlink]
            clicks_data[long_url] = clicks_data.get(long_url, 0) + 1
    
    output = []
    for long_url, clicks in clicks_data.items():
        output.append({long_url: clicks})
    return output


def main():
    encodes = read_encodes_csv('encodes.csv')
    decodes = read_decodes_json('decodes.json') 
    filtered_decodes = filter_decodes_by_year(decodes, 2021)
    clicks_data = calculate_clicks(encodes, filtered_decodes)
    print(clicks_data)
  

if __name__ == '__main__':
    main()
