import json

def convert_to_json(dataframe, filename):
    
    """
    This function converts the input DataFrame to a JSON file with the specified filename.
    """
    
    print("Creating JSON file...")
    
    json_data = []
    for index, row in dataframe.iterrows():
        json_data.append({'chiave': index+1, 'valore': row.to_dict()})
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    
    print("JSON file saved ✔️ \n")