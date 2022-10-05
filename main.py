import requests

url = "https://api.transpose.io/nft/sales-by-account?account_address=0x175A8FF49660fd7c168a77142C22389d4430b876&role=all&order=asc&limit=100"

headers = {
    "accept": "application/json",
    "x-api-key": "gDvSKYoJJT7BckVawmrss6rzWHp4R2mdazwuyUXl"
}

response = requests.get(url, headers=headers)

r = response.json()

total_sales = len(r['results'])
print(f"Total sales: {total_sales}")

#Create buyers list:
buyers = []
for i in range(total_sales):
    buyers.append(r['results'][i]['buyer'])

print("List of buyers:")
print(*buyers, sep = "\n")
