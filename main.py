import requests
import json
import yaml
import pandas as pd
from io import StringIO

def get_content(url, headers):
    """
    This function makes a GET request to the specified url and returns the content of the response.
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Error status code:", response.status_code)
        return ""

def convert_to_csv(content, filename):
    """
    This function converts the input content to a CSV file with the specified filename.
    """
    with open(filename, "w") as csv_file:
        csv_file.write(content)
    print("CSV file saved")

def convert_to_json(dataframe, filename):
    """
    This function converts the input DataFrame to a JSON file with the specified filename.
    """
    json_data = []
    for index, row in dataframe.iterrows():
        json_data.append({'chiave': index+1, 'valore': row.to_dict()})
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    print("JSON file saved")

def convert_to_yaml(dataframe, filename):
    """
    This function converts the input DataFrame to a YAML file with the specified filename.
    """
    yaml_data = []
    for index, row in dataframe.iterrows():
        yaml_data.append({'chiave': index+1, 'valore': row.to_dict()})
    with open(filename, "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file)
    print("YAML file saved")

def main():
    url = "https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true"
    headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    content = get_content(url, headers)
    if content == "":
        print("Error: Could not retrieve content from the specified url")
        return
    convert_to_csv(content, "PIRC.csv")
    dataframe = pd.read_csv(StringIO(content))
    convert_to_json(dataframe, "PIRC.json")
    convert_to_yaml(dataframe, "PIRC.yaml")

if __name__ == "__main__":
    main()
