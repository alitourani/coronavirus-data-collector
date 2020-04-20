from matplotlib import pyplot as plt
import OpenBlender
import pandas as pd
import json
%matplotlib inline

action = 'API_getObservationsFromDataset'
parameters = { 
 """
 Sign-up in https://www.openblender.io/ and download dataset from https://www.openblender.io/#/dataset/explore/5e7a0d5d9516296cb86c6263/or/35
 Then, go to Account -> API TOKEN and replace the generated token with the below string:
 """
 'token' : 'something',
 'id_dataset' : '5e7a0d5d9516296cb86c6263',
 'date_filter' : {
               "start_date":"2020-01-01T06:00:00.000Z",
               "end_date":"2020-03-11T06:00:00.000Z"},
 'consumption_confirmation' : 'on',
 'add_date' : 'date'
}

df_confirmed = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df_confirmed.reset_index(drop=True, inplace=True)
df_confirmed.head(10)