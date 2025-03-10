import pandas as pd

#criação de data frame
dados = pd.DataFrame(
    {   'Nome': ['Daniel', 'Vilma', 'Isabela', 'Osvaldo'],
        'Idade': [31, 36, 15,38],
        'Sexo': ['Masculino', 'Feminino', 'Feminino', 'Masculino']
            
    }
)

#a linha abaixo exporta as informações sem indice

dados.to_csv('arquivo_exportado.csv', index=False)