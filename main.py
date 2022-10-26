import requests
from termcolor import colored
import numpy as np

Whale_contract_address = '0x175A8FF49660fd7c168a77142C22389d4430b876'
OpenSea_contract_address = '0x495f947276749Ce646f68AC8c248420045cb7b5e'

unique = True
# To print only unique addresses
def _print(b):
    if unique:
        print(*np.unique(np.array(b)), sep="\n")
    else:
        print(*b, sep="\n")
    print("##########################################")

url = f"https://api.transpose.io/nft/sales-by-account?account_address={Whale_contract_address}&role=all&order=asc&limit=100"

headers = {
    "accept": "application/json",
    "x-api-key": "gDvSKYoJJT7BckVawmrss6rzWHp4R2mdazwuyUXl"
}

response = requests.get(url, headers=headers)

r = response.json()

total_sales = len(r['results'])
print(colored(f"Total sales: {total_sales}","green"))

# Create buyers list and tokenId list:
buyers = []
tokenId = []
for i in range(total_sales):
    buyers.append(r['results'][i]['buyer'])
    tokenId.append(r['results'][i]['token_id'])

# Note that the i-th buyer in the list bought the i-th NFT in the tokenId list
print(colored("List of buyers:","green"))
_print(buyers)

# Print list of TokenIDs
# print("List of TokenIDs:")
# print(*tokenId, sep="\n")

# Check if primary buyers still hold the NFT:
print(colored("Checking owners, holders and sellers ...","green"))
owners = []
for tok_id in tokenId:
    url2 = f"https://api.transpose.io/nft/owners-by-token-id?contract_address={OpenSea_contract_address}&token_id={tok_id}&limit=100"
    response2 = requests.get(url2, headers=headers)
    r2 = response2.json()
    if r2['results']: # check if results is non-empty
        owners.append(r2['results'][0]['owner'])
    else:
        owners.append(0)

print(colored("List of all whale owners:","green"))
owners_fil = list(filter(lambda x: x != 0, owners))
_print(owners_fil)
# Now we filter out the buyers who are not owners
holders = []
sellers = []
for i in range(total_sales):
    if buyers[i] == owners[i]:
        holders.append(buyers[i])
    else:
        sellers.append(buyers[i])

print(colored(f"Number of holders: {len(holders)}", "green"))
print(colored("List of Holders:", "green"))
_print(holders)
sellers = list(filter(lambda x: x != Whale_contract_address, sellers))
print(colored("List of people who sold their whale:","green"))
_print(sellers)


