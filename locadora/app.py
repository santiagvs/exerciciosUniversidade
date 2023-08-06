import os

TAXA_DIARIA = 70
TAXA_POR_KM = 0.10

def cadastro_geral(clientes):
  while True:
    os.system('clear')
    nome_do_cliente = input("Digite aqui o nome do cliente: ")
    sexo = cadastro_sexo()
    placa_do_carro = input("Digite aqui a placa do carro: ")
    qtd_km_contratados = int(input("Digite a quantidade de km contratados: "))
    qtd_dias_contratados = int(input("Digite a quantidade de dias contratados: "))

    cliente = {
      "nome": nome_do_cliente,
      "sexo": sexo,
      "placa": placa_do_carro,
      "km": qtd_km_contratados,
      "dias": qtd_dias_contratados,
      "valor_total": 0
    }

    cliente["valor_total"] = TAXA_DIARIA * cliente["dias"] + TAXA_POR_KM * cliente["km"]

    clientes.append(cliente)

    if input("Deseja inserir mais dados? Digite 's' se sim, e 'n' se não: ") != 's':
      break

def cadastro_sexo():
  while True:
    sexo = input("Digite F para *feminino* e M para *masculino*: ")
    if sexo in ["F", "M"]:
      break
    print("Por favor, digite o sexo de acordo com os caracteres F ou M.")
