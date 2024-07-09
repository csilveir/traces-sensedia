import json

# Ler o arquivo JSON
with open("data/table-full.json", "r") as file:
    data = json.load(file)

# Processar os dados conforme o critério
for item in data:
    attributes = item.get("attributes", {})
    attributes.pop("http.request.headers", None)
    attributes.pop("sensedia.trace", None)
    attributes.pop("http.response.headers", None)

# Salvar o resultado processado em um novo arquivo JSON
with open("data/table-metrics.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Objetos processados e salvos em table-metrics.json")