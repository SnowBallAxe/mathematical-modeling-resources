cities = {
    "Tokyo": {
        "countary": "Japan",
        "population": "14.27 million",
        "fact": "Tokyo is the largest metropolitan area on Earth.",
    },
    "New York": {
        "countary": "USA",
        "population": "8.58 million",
        "fact": "Speakers use around 800 different languagesin New York.",
    },
    "Shanghai": {
        "countary": "China",
        "population": "24.58 million",
        "fact": "Shanghai features the  longest metro network in the world.",
    },
}

for city, city_info in cities.items():
    print(f"\nCity name: {city}")
    print(f"{city} is in {city_info['countary']}.")
    print(f"It's population is {city_info['population']}.")
    print(city_info["fact"])
