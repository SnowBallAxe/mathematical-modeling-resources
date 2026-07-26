river_country = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
}
for river, country in river_country.items():
    print(f"The {river} runs through {country}.")

for river in river_country.keys():
    print(river)

for country in set(river_country.values()):
    print(country)
