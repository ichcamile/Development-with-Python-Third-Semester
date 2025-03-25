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
    inserir = """INSERT INTO cadastros(id, nome, cidade, uf, email, valor) VALUES (%s, %s, %s, %s, %s, %s)"""

    qtd = 0

    for linha in dados_csv:
        coluna = [item.strip() for item in linha.split(';')]  # Limpar espaços e dividir os valores

        # Ignorar o cabeçalho
        if coluna[0].upper() == 'ID':
            continue

        # Criar os valores para inserção
        valores = (int(coluna[0]), coluna[1], coluna[2], coluna[3], coluna[4], float(coluna[5]))

        # Inserir o registro
        cursor.execute(inserir, valores)

        qtd += 1

# Confirmar e fechar conexão
conexao.commit()
conexao.close()

print(f"Quantidade Total de Registros: {qtd}")
