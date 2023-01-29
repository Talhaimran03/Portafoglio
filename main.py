# Import of libraries
import pandas as pd
from io import StringIO
import os

# Import of the functions
from scripts.get_content import get_content
from scripts.save_csv import save_csv
from scripts.convert_to_json import convert_to_json
from scripts.convert_to_yaml import convert_to_yaml

def main():

    """
    The main manages the functions
    """
    
    url = "https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true"
    headers = {"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    content = get_content(url, headers)
    if content == "":
        print("Error: Could not retrieve content from the specified url")
        return # If error exit from main()

    # Reads the content of the CSV file and converts it into a DataFrame, 
    # which is a two-dimensional size-mutable, tabular data structure with rows and columns.
    dataframe = pd.read_csv(StringIO(content))

    # Check if the output_files directory exists, if not create it
    path = "output_files"
    if not os.path.exists(path):
        print("Creating the output file directory...\n")
        os.makedirs(path)
    else:
        # Iterate through all files in the output_files directory and remove them
        print("Removing the oldest files from directory...\n")
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Saving the csv file
    save_csv(content, path + "/PIRC.MI.csv")

    # Converting the dataframe into JSON and YAML
    convert_to_json(dataframe, path + "/PIRC.MI.json")
    convert_to_yaml(dataframe, path + "/PIRC.MI.yaml")

    print("Writing completed successfully ✔️ \n")

if __name__ == "__main__":
    main()
