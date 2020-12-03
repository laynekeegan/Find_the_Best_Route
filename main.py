"""
Project 2 for CS 118: Layne Keegan
Given five cities, this program will find the best route through those cities in five days. Our "best
route" is based on the highest average temperature, while still considering our budget.
"""
from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}
cities = list(city_temps.keys())
hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}
hotels = list(hotel_rates.keys())
HOTEL_BUDGET = 850
DAYS = 5


def best_temp(t):
    """The best_temp() function will find the best route based upon the highest average temperature in each city."""
    s = 0
    for i in t:
        s += max(city_temps[i])
    return s


temp_perms = permutations(cities, DAYS)
best = max(temp_perms, key=lambda t: best_temp(t))
average_temp = (best_temp(best)/DAYS)


def costs(t):
    """The costs() function will find the cheapest combination of hotels on the trip."""
    return sum([hotel_rates[x] for x in t])


hotel_combs = list(combinations_with_replacement(hotels, DAYS))
best_option = min(hotel_combs, key=lambda t: HOTEL_BUDGET - costs(t) if HOTEL_BUDGET >= costs(t) else HOTEL_BUDGET)
total_cost = costs(best_option)

if __name__ == "__main__":
    print(f'Here is your best route: {best} the average of the daily max temp. is {average_temp}°F')
    print(f'To max out your hotel budget, stay at these hotels: {best_option}, totaling ${total_cost}')
