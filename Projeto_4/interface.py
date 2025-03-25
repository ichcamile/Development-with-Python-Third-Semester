from tkinter import *
import pandas as pd  # Importar a biblioteca pandas

class Aplicacao:
    def __init__(self):
        # Criar a janela principal
        self.layout = Tk()

        # Configurar a janela
        self.layout.title("Gerador de Relatórios")
        self.layout.geometry("300x150")

        # Vincular os widgets à janela principal
        self.tela = Frame(self.layout)
        self.tela.pack(pady=10)

        # Criar e adicionar os widgets
        self.descricao = Label(self.tela, text="Clique no botão para exportar o arquivo CSV:")
        self.descricao.pack()

        self.exportar = Button(self.tela, text="Gerar Arquivo", command=self.exportar_arquivo)
        self.exportar.pack(pady=10)

        self.status = Label(self.tela, text="", fg="green")  # Para exibir mensagens de status
        self.status.pack()

        # Iniciar o loop principal do Tkinter
        self.layout.mainloop()

    def exportar_arquivo(self):
        # Criação de um dataframe
        dados = pd.DataFrame(
            {
                'Nome': ['Daniel', 'Vilma', 'Isabella', 'Osvaldo'],
                'Idade': [31, 36, 2, 38],
                'Sexo': ['M', 'F', 'F', 'M']
            }
        )

        # Exportar as informações para CSV
        try:
            dados.to_csv('arquivo_exportado_sem_indice.csv', index=False)
            self.status.config(text="Arquivo exportado com sucesso!", fg="green")
        except Exception as e:
            self.status.config(text=f"Erro ao exportar: {e}", fg="red")


# Criar uma instância da aplicação
tl = Aplicacao()
