# Breutzmann, Robert
# CSD 325 - Advanced Python
# Assignment 7.2
# Due Date - 11/24/25

def combineCity(city, country, population: int = None, lang = None):
    result = f"{city}, {country}"
    if population:
        result += f" population - {population:,}"
    if lang:
        result += f", {lang}"
    return result

city1 = "Madrid"
country1 = "Spain"
city2 = "Rome"
country2 = "Italy"
population2 = 2750000
city3 = "Berlin"
country3 ="Germany"
population3 = 37000000
language3 = "German"
city4 = "Tripoli"
country4 = "United States"
language4 = "English"
combined1 = combineCity(city1, country1)
combined2 = combineCity(city2, country2, population2)
combined3 = combineCity(city3, country3, population3, language3)
combined4 = combineCity(city4, country4, language4)

print(combined1)
print(combined2)
print(combined3)
print(combined4)