import requests

Whale_contract_address = '0x175A8FF49660fd7c168a77142C22389d4430b876'
OpenSea_contract_address = '0x495f947276749Ce646f68AC8c248420045cb7b5e'

url = f"https://api.transpose.io/nft/sales-by-account?account_address={Whale_contract_address}&role=all&order=asc&limit=100"

headers = {
    "accept": "application/json",
    "x-api-key": "gDvSKYoJJT7BckVawmrss6rzWHp4R2mdazwuyUXl"
}

response = requests.get(url, headers=headers)

r = response.json()

total_sales = len(r['results'])
print(f"Total sales: {total_sales}")

# Create buyers list and tokenId list:
buyers = []
tokenId = []
for i in range(total_sales):
    buyers.append(r['results'][i]['buyer'])
    tokenId.append(r['results'][i]['token_id'])

# Note that the i-th buyer in the list bought the i-th NFT in the tokenId list
print("List of buyers:")
print(*buyers, sep="\n")

# Print list of TokenIDs
# print("List of TokenIDs:")
# print(*tokenId, sep="\n")

# Check if primary buyers still hold the NFT:
print("Checking holders ...")
owners = []
for tok_id in tokenId:
    url2 = f"https://api.transpose.io/nft/owners-by-token-id?contract_address={OpenSea_contract_address}&token_id={tok_id}&limit=100"
    response2 = requests.get(url2, headers=headers)
    r2 = response2.json()
    if r2['results']: # check if results is non-empty
        owners.append(r2['results'][0]['owner'])
    else:
        owners.append(0)

# Now we filter out the buyers who are not owners
holders = []
for i in range(total_sales):
    if buyers[i] == owners[i]:
        holders.append(buyers[i])

print(f"Number of holders: {len(holders)}")
print("List of Holders:")
print(*holders, sep="\n")


