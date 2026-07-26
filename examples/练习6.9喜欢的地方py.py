favourite_places = {
    "Alice": ["Shanghai", "Tokyo"],
    "Mike": ["New York"],
    "Jean": ["Los Angelos", "London", "Hong Kong"],
}

for name, places in favourite_places.items():
    print(f"\n{name} likes:")
    for place in places:
        print(f"- {place}")
