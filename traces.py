import json

# Ler o arquivo JSON
with open("data/table-full.json", "r") as file:
    data = json.load(file)

# Processar os dados conforme o critério
result_list = []
for item in data:
    attributes = item.get("attributes", {})
    filtered_attributes = {
        "http.request.headers": attributes.get("http.request.headers"),
        "sensedia.trace": attributes.get("sensedia.trace"),
        "http.response.headers": attributes.get("http.response.headers")
    }
    item["attributes"] = filtered_attributes
    result_list.append(item)

# Salvar o resultado processado em um novo arquivo JSON
with open("data/table-trace-headers.json", "w") as outfile:
    json.dump(result_list, outfile, indent=4)

print(f"{len(result_list)} objetos processados e salvos em table-trace-headers.json")