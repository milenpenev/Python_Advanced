countries = input().split(", ")
capitals = input().split(", ")

countries_capitals = {country:capital for country, capital in zip(countries, capitals) }
print('\n'.join([f"{key} -> {value}" for key, value in countries_capitals.items()]))