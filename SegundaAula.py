nome = input("Digite o nome do funcionario: ")
salario_bruto = float(input("Digite o valor do seu salário bruto:  "))

VA = salario_bruto * 0.05
VT = salario_bruto * 0.06
INSS = salario_bruto * 0.11
auxilio_creche = 0.0

indicador = input("Você usufrui o auxilio creche? (S) Sim | (N) Não  ").upper()

if indicador == "S":
    auxilio_creche = salario_bruto * 0.15
else:
    auxilio_creche = 0 

salario_liquido = salario_bruto - (VA + VT + INSS + auxilio_creche)

print(f"{nome} seu salario liquido é R$ {salario_liquido}")
print(f"Total de descontos R$ {VA + VT + INSS + auxilio_creche} \n Sendo {VA} de Vale Alimentação \n {VT} de Vale Transporte, \n {INSS} de INSS \n e {auxilio_creche} de Auxilio Creche")


