it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Telegram", "WhatsApp", "Snapchat"])
print(it_companies)

it_companies.remove("Microsoft")
print(it_companies)

it_companies.discard("Samsung")
print(it_companies)

#The difference between remove and discar is If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

