import requests

def get_content(url, headers):
    
    """
    This function makes a GET request to the specified url and returns the content of the response.
    """
    
    print("\nRequesting file...")
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Request successful ✔️ \n")
        return response.text
    else:
        print("Error status code ❌:", response.status_code)
        return ""