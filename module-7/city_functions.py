# Breutzmann, Robert
# CSD 325 - Advanced Python
# Assignment 7.2
# Due Date - 11/24/25

def combineCity(city, country, population: int = None, lang):
    result = f"{city}, {country}"
    if population:
        result += f" population - {population:,}"
    return result

city1 = "Madrid"
country1 = "Spain"
city2 = "Rome"
country2 = "Italy"
city3 = "Berlin"
country3 ="Germany"
combined1 = combineCity(city1, country1)
combined2 = combineCity(city2, country2)
combined3 = combineCity(city3, country3)

print(combined1)
print(combined2)
print(combined3)