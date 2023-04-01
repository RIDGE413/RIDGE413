import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os

#checks if this folder exists
path= r'C:\Users\RIDGE\.kaggle'
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
    print(".kaggle created in C:\x5cUsers\x5cRIDGE\x5c")
    

#access the API
api = KaggleApi()
api.authenticate()

#download dataset
api.dataset_download_file('world-happiness-report-2023', 'WHR2023.csv')
 
#  test