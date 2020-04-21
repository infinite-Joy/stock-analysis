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
stocks = ['timestamp', 'tcs', 'infosys', 'hcl', 'tech mahindra', 'oracle finserv', 'mphasis']
original_cols = [c for c in stocks if c != 'timestamp']
df = pd.DataFrame(columns=stocks)
for filename in onlyfiles:
    with open(filename) as f:
        overall_info = {}
        for line in f:
            overall_info = process_line(line, overall_info)
    df = df.append(overall_info, ignore_index=True)
    print('done reading', filename)


df = df.set_index('timestamp')
df = df.sort_index()

# now that we have all the df in place we will need to normalise them
# so that the analysis can be done on an equal level field.
# we will do percentage change from previous
for col in original_cols:
    pc_col = col + '_pc'
    df[pc_col] = df[col].pct_change()
print('percentage_change calculation done')


def is_too_deviated(percentage_change, mean, std):
    """we will say that the stock is too deviated
    if the different from the industry mean
    is more than 2 sigma
    """
    diff = percentage_change - mean
    return diff > 2 * std

# taking the mean of the change in the peer level values.
pc_cols = [c for c in df.columns if 'pc' in c]
df['mean_across_peers'] = df[pc_cols].mean(axis=1)
df['std_dev_across_peers'] = df[pc_cols].std(axis=1)
print('mean and std dev across peers done')
df = df.fillna(0.0)
for percentage_change in pc_cols:
    is_deviated = percentage_change + '_dev'
    df[is_deviated] = df.apply(lambda x: is_too_deviated(x[percentage_change], x['mean_across_peers'], x['std_dev_across_peers']), axis=1)

df.to_csv('out.csv')
print('all done and saved to out.csv')
