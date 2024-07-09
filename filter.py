import json

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        return json.load(arquivo)
def testar_parent_span_id_nao_nulo(dicionario):
    return len(dicionario.get("parentSpanId")) == 0 

def extrair_spans(dados):
    spans_extraidos = []
    resource_spans = dados.get("resourceSpans", [])
    if resource_spans:
        scope_spans = resource_spans[0].get("scopeSpans", [])
        for scope in scope_spans:
            spans = scope.get("spans", [])
            for span in spans:
             if testar_parent_span_id_nao_nulo(span):
                spans_extraidos.append(span)
    return spans_extraidos

caminho_arquivo = "data/traces.json"

dados = ler_arquivo_json(caminho_arquivo)

spans = extrair_spans(dados)

json_file_name = "data/resultado.json"

json_file = open(json_file_name, encoding="utf8", mode="w")
json_file.truncate()

json_file.write("[")
for span in spans:
    json.dump(span, json_file, indent=4, separators=(",", ":"))

json_file.write("]")    
json_file.close()

data = None

with open(r'data/resultado.json', 'r') as file: 
  
    data = file.read() 
    data = data.replace("}{", "},{") 

with open(r'data/resultado.json', 'w') as file: 

    file.write(data)     

print(f"{len(spans)} objetos processados e salvos em resultado.json")