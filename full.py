import json

# Função auxiliar para converter a lista de atributos em um dicionário
def attributes_to_dict(attributes):
    result = {}
    for attribute in attributes:
        key = attribute.get("key")
        value = attribute.get("value")
        if key and value:
            for v in value.values():
                result[key] = v
    return result

# Ler o arquivo JSON
with open("data/resultado.json", "r") as file:
    data = json.load(file)

# Processar os dados conforme o critério
result_list = []
for item in data:
    attributes = item.get("attributes", [])
    item["attributes"] = attributes_to_dict(attributes)
    result_list.append(item)

# Salvar o resultado processado em um novo arquivo JSON
with open("data/table-full.json", "w") as outfile:
    json.dump(result_list, outfile, indent=1)

print(f"{len(result_list)} objetos processados e salvos em table-full.json")