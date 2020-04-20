from datetime import datetime
from os import listdir
from os.path import isfile, join
import pandas as pd

mypath = '.'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = [f for f in onlyfiles if '.txt' in f]
print(onlyfiles)

def process_line(line, overall_info={}):
    if 'company' in line:
        company_info, price_info = line.strip().split(';')
        company, company_name = company_info.strip().split(':')
        company_name = company_name.strip()
        price, price_amnt = price_info.strip().split(':')
        price_amnt = float(price_amnt)
        return {**overall_info, company_name: price_amnt}
    else:
        # this is for header
        line = line.strip()
        datetime_object = datetime.strptime(line, '%Y-%m-%d %H:%M:%S.%f')
        return {**overall_info, 'timestamp': datetime_object}



all_infos = []
df = pd.DataFrame(columns=['timestamp', 'tcs', 'infosys', 'hcl', 'tech mahindra', 'oracle finserv', 'mphasis'])
for filename in onlyfiles:
    with open(filename) as f:
        overall_info = {}
        for line in f:
            overall_info = process_line(line, overall_info)
    df = df.append(overall_info, ignore_index=True)
    print('done reading', filename)


df = df.set_index('timestamp')
df = df.sort_index()
print(df)
