import pandas as pd
import plotly.express as px

arquivo = pd.read_excel(r'C:\Users\camil\Downloads\Estudos_Faculdade\Development-with-Python-Third-Semester\Projeto_2\formula1.xlsx', engine='openpyxl')

pilotos = arquivo['PILOTO']
pontos = arquivo['PONTOS']

grafico = px.bar(x=pilotos, y=pontos, width=1000, height=700, title="Pontos dos Pilotos")

grafico.show()