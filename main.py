import time
import csv
import pandas as pd
import requests

SLEEP = 0
url_list = []
url_statuscodes = []

def getStatusCode(url):
    try:
        r = requests.head(url, verify=False, timeout=5)
        return r.status_code

    except Exception as e:
        return e

if __name__ == '__main__':

    with open('check.txt', newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            url_list.append(row[0])
    
    for url in url_list:
        print(url)
        check = [url, getStatusCode(url)]
        time.sleep(SLEEP)
        url_statuscodes.append(check)

    df = pd.DataFrame(url_statuscodes, columns=['URL', 'Statuscode'])
    df.to_csv('finish.csv')