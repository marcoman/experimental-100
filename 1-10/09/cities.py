# nesting dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], 
               "total_visits": 4},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                "total_visits": 5},
}


travel_log_2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], 
               "total_visits": 4,
               "favorite_food": ["Pizza",]
               },
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
                "total_visits": 5,
                "favorite_food": ["Pizza", "Burger"]},
}

travel_log_3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 4,
        "favorite_food": ["Pizza",]
     },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
        "favorite_food": ["Pizza", "Burger"],
    }
]


print (travel_log["France"])
print (travel_log["Germany"])

print (travel_log_2["France"]["favorite_food"])
print (travel_log_2["Germany"]["favorite_food"])
