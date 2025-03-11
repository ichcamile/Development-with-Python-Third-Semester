import pandas as pd

arquivo = pd.read_csv(r"C:\Users\camil\Downloads\Estudos_Faculdade\Development-with-Python-Third-Semester\Projeto_3\importar\base.csv", sep=";")

print(f"Total de Registros {arquivo['NOME'].count() }")

print(f"O maior valor {arquivo['VALOR'].max() }")

print(f"a média do valor {arquivo['VALOR'].mean() }")

print(f"o menor valor {arquivo['VALOR'].min() }")

print(f"Valor total {round(arquivo['VALOR'].sum(),2) }")

email_google = 0

for email in arquivo['EMAIL']:
    if email.find("gmail") > 0:
        email_gmail += 1

print(f"Total de E-mails gmail: {email_google}")