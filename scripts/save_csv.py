def save_csv(content, filename):

    """
    This function writes the content in a CSV file with the specified filename.
    """

    print("Saving csv file...")

    with open(filename, "w") as csv_file:
        csv_file.write(content)
    
    print("CSV file saved ✔️ \n")