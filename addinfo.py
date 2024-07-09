import json

# Função auxiliar para filtrar e mover os atributos
def process_attributes(attributes):
    additional_info = {k: v for k, v in attributes.items() if k.startswith("sensedia.additional_info")}
    filtered_attributes = {k: v for k, v in attributes.items() if not k.startswith("sensedia.additional_info")}
    return additional_info, filtered_attributes

# Ler o arquivo JSON
with open("data/table-metrics.json", "r") as file:
    data = json.load(file)

# Processar os dados conforme o critério
for item in data:
    attributes = item.get("attributes", {})
    additional_info, filtered_attributes = process_attributes(attributes)
    item["additionalInfo"] = additional_info
    item["attributes"] = filtered_attributes

# Salvar o resultado processado em um novo arquivo JSON
with open("data/table-metrics-addinfo.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print(f"Objetos processados e salvos em table-metrics-addinfo.json")