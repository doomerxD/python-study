import requests
import json

try:
    results = []
    pokemons =["pikachu", "bulbasaur", "charmander"]
    for pokemon in pokemons:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        data = response.json()
        pokemon_data = {
            "name": data["name"],
            "weight": data["weight"],
            "type": data["types"][0]["type"]["name"]
        }
        results.append(pokemon_data) 
        print(f"{pokemon_data['name']} を取得しました")

    with open("results.json", "w", encoding="UTF-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("results.json に保存完了！")

except requests.exceptions.ConnectionError:
    print("ネットワークに接続できませんでした")