import yaml

def convert_to_yaml(dataframe, filename):

    """
    This function converts the input DataFrame to a YAML file with the specified filename.
    """
    
    print("Creating YAML file...")

    yaml_data = []
    for index, row in dataframe.iterrows():
        yaml_data.append({'chiave': index+1, 'valore': row.to_dict()})
    with open(filename, "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file)
        
    print("YAML file saved ✔️ \n")