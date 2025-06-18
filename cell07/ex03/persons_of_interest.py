def famous_births(scientists):
    for key, value in scientists.items():
        print(f"{value['name']} was born in {value['date_of_birth']}.")

woman_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace HOpper", "date_of_birth": "1906" }
}   

famous_births(woman_scientists)