import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='toor', 
    db='aula'
)

cursor = conexao.cursor()

# Abrir o arquivo CSV corretamente
with open('base.csv', 'r', encoding='utf-8') as dados_csv:

    inserir = 'INSERT INTO cadastros(id, nome, cidade, uf, email, valor) VALUES (%s, %s, %s, %s, %s, %s)'

    valores = []  # Criar uma lista para armazenar os dados
    qtd = 0

    for linha in dados_csv:
        coluna = linha.strip().split(';')  # Remover espaços extras e dividir os valores

        # Ignorar o cabeçalho
        if coluna[0].upper() == 'ID':
            continue

        try:
            # Adicionar os valores à lista (convertendo corretamente os tipos)
            valores.append((int(coluna[0]), coluna[1], coluna[2], coluna[3], coluna[4], float(coluna[5])))
            qtd += 1
        except ValueError:
            print(f"Erro ao processar linha: {linha}")  # Exibir erro caso os dados estejam mal formatados

# Executar a inserção apenas se houver