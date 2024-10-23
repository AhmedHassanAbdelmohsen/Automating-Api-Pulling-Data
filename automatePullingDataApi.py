import time

import requests
import pandas as pd
import  json
import datetime
from datetime import datetime
while True:
    timestamp = datetime.now()

    url = 'https://disease.sh/v3/covid-19/countries'
    page = requests.get(url, params='parameters')
    data = page.json()
    df = pd.json_normalize(data)
    df['timestamp'] = timestamp
    cols = ['timestamp'] + [col for col in df.columns if col != 'timestamp']
    df = df[cols]
    df.to_csv(r'C:\Users\Ahmed Hassan\Documents\python for begginer\csvFiles\covidData.csv', mode='a',
              index=False, header=False)
    time.sleep(30)

    print('already done')

