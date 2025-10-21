import csv

# Dados para escrever no arquivo
dados = [
    ['Nome', 'Idade'],
    ['João', 30],
    ['José', 27],
    ['Maria', 25]
]

# Abre o arquivo 'meus_dados.csv' em modo de escrita
with open('meus_dados.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    # Cria um objeto de escrita CSV
    escritor = csv.writer(arquivo_csv)
    
    # Escreve as linhas no arquivo
    for linha in dados:
        escritor.writerow(linha)

print("Arquivo 'meus_dados.csv' criado com sucesso!")

# Exemplo com DictWriter (escrevendo dicionários)
dados_dict = [
    {'Nome': 'Ana', 'Idade': 32},
    {'Nome': 'Pedro', 'Idade': 29}
]

with open('meus_dados_dict.csv', 'w', newline='', encoding='utf-8') as arquivo_csv_dict:
    # Define o cabeçalho
    campos = ['Nome', 'Idade']
    escritor_dict = csv.DictWriter(arquivo_csv_dict, fieldnames=campos)
    
    # Escreve o cabeçalho
    escritor_dict.writeheader()
    # Escreve as linhas
    escritor_dict.writerows(dados_dict)

print("Arquivo 'meus_dados_dict.csv' criado com sucesso!")