river_countary={
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
}
for river,countary in river_countary.items():
    print(f"The {river} runs through {countary}.")

for river in river_countary.keys():
    print(river)

for countary in set(river_countary.values()):
    print(countary)