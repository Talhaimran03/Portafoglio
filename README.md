# Portafoglio
![Author](https://img.shields.io/badge/author-Oliverio%20Lorenzo,%20%20Pavoni%20Alberto,%20%20Imran%20Talha,%20%20Kasun%20Rajapaksha-blue)
![Language](https://img.shields.io/badge/language-python-orange?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Linux-blue?style=flat)
![Testing](https://img.shields.io/badge/version-v01.01-green)

![](https://www.zdnet.com/a/img/resize/0a6b0be2f543ddbf313fc83a706b807b77c3c202/2021/07/19/8a337c80-5ed6-43a1-98fb-b981d420890f/programming-languages-shutterstock-1680857539.jpg?auto=webp&fit=crop&height=900&width=1200)

***

## Description

- Python program which downloads the csv file from yahoo finance
- Converts the csv file into json and then into yaml

## Required

- Python version between `3.6` and `3.9`
- `requests` library
 ```commandline
    pip install request
 ```
    
- `csv` library
 ```commandline
    pip install csv
 ```

- `json` library
 ```commandline
    pip install json
 ```
    
- `Yaml` library
 ```commandline
    pip install PyYAML
 ```
    
- `pandas` library
 ```commandline
    pip install pandas
 ```
 
 ## Check list
**Research** 
- [x] Analysing and studying of the assignment                    
- [x] Research and data collection                                
- [x] WBS, RACI, OBI compilation                                  

**DEVELOPMENT**                                             
- [x] Choice of language to use                                   
- [x] Choice of libraries to use                                  
- [x] source code development                                     
- [x] Testing the script                                          
- [x] Solving bugs                                                
- [x] Advance search on google to resolve unspected problems      

**Submit process**                                          
- [x] Dividing the script in files by functions                   
- [x] Adding comments to the script                               
- [x] Creating and compiling the markdown file                    
- [x] Sharing the completed project work with group               
- [x] Studying and resolving problems  (in case have any)         
- [x] Creating Repository in GitHub and submitting the projecDoing
- [x] **Presentation of completed Project**                                            


## Execution examples

Open a terminal with path "./portafoglio/" and type the following command:

- Windows:
  ```
  python main.py
  ```

- Linux:
  ```
  python3 main.py
  ```
## Output example

Requesting file...
Request successful ✔️ 

Removing the oldest files from directory...

Saving csv file...
CSV file saved ✔️ 

Creating JSON file...
JSON file saved ✔️ 

Creating YAML file...
YAML file saved ✔️ 

Output files saved successfully in directory "output files" ✔️
Execution completed successfully ✔️ 


- PIRC.MI.csv:  
  Date,Open,High,Low,Close,Adj Close,Volume  
  2022-01-24,6.386000,6.424000,6.058000,6.088000,5.870860,2370106  
  2022-01-25,6.176000,6.256000,6.110000,6.200000,5.978866,2014242  

- PIRC.MI.json:  
   {  
       "chiave": 1,  
       "valore": {  
           "Date": "2022-01-24",  
           "Open": 6.386,  
           "High": 6.424,  
           "Low": 6.058,  
           "Close": 6.088,  
           "Adj Close": 5.87086,  
           "Volume": 2370106  
       }  
   },  
   {  
       "chiave": 2,  
       "valore": {  
           "Date": "2022-01-25",  
           "Open": 6.176,  
           "High": 6.256,  
           "Low": 6.11,  
           "Close": 6.2,  
           "Adj Close": 5.978866,  
           "Volume": 2014242  
     }  

- PIRC.MI.yaml:  
   - chiave: 1  
     valore:  
       Adj Close: 5.87086  
       Close: 6.088  
       Date: '2022-01-24'  
       High: 6.424  
       Low: 6.058  
       Open: 6.386  
       Volume: 2370106  
   - chiave: 2  
     valore:  
       Adj Close: 5.978866  
       Close: 6.2  
       Date: '2022-01-25'  
       High: 6.256  
       Low: 6.11  
       Open: 6.176  
       Volume: 2014242  
  
  
## Tags

 **#markdown, #tags, #python, #circular_programming**

***

## Author

Made by Oliverio Lorenzo, Pavoni Alberto, Imran Talha, Kasun Rajapaksha

## Contact

If you have any problem please contact us:
> 19133@studenti.marconiverona.edu.it,
> 19211@studenti.marconiverona.edu.it,
> 19078@studenti.marconiverona.edu.it,
> 18732@studenti.marconiverona.edu.it
 
 ## Repository's link
 
 https://github.com/Talhaimran03/Portafoglio
 
