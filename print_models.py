import json

if __name__ == "__main__":
    models_file = 'resources/chatgpt_models_2023-03-03.json'
    with open(models_file) as models_json:
        models = json.load(models_json)
        models_list = []
        for model in models["data"]:
            models_list.append(model["id"])
        models_list.sort()
        print(models_list)
