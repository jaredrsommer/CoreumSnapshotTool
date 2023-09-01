from pycosmicwrap import CosmicWrap
import json
import pandas as pd
import datetime


# put your address here
validator = 'corevaloper1uhrrdv6g6v9t38v4qghjucunnxyk8xt30vr8za'
n = 0
data = []

print("Starting Snapshot")
# create an object with rest api url, rpc url and denom as arguments
core = CosmicWrap(lcd='https://rest-coreum.ecostake.com/',
                       rpc='https://rpc-coreum.ecostake.com/',
                       denom='ucore')

snap = core.query_delegators(validator)

for d in snap:
    n = n+1
    wallet = d['delegation']['delegator_address'] 
    delegation = float(d['delegation']['shares'])*0.000001
    data.append({
        'Wallet': wallet,
        'Delegation': delegation,
        })
    print(f"Wallet #{n}: {wallet} Delegation: {delegation:.6f}")
    df = pd.DataFrame(data)
    current_date = datetime.datetime.now()
    month_abbreviation = current_date.strftime('%b')
    new_file_name = f"{month_abbreviation}_snapshot.csv"
    df.to_csv(new_file_name, index=False)
print("Writing Snapshot to File")
print("total delegators:", n)
print("Snapshot complete!")