import app

clientes = []

while True:
  app.cadastro_geral(clientes)

  print("\nValor total pago por placa:")
  for cliente in clientes:
    print(f"- {cliente['placa']}: R${cliente['valor_total']:.2f}")

  km_total = sum(cliente['km'] for cliente in clientes)
  numero_clientes = len(clientes)
  media_km_contratados = km_total / numero_clientes
  print(f"\nMédia de quilomêtros contratados: {media_km_contratados} km")

  print("\nClientes de sexo feminino que fecharam aluguéis acima de 7 dias contratados:")
  for cliente in clientes:
    if cliente["sexo"] == "F" and cliente["dias"] > 7:
      print(f"- {cliente['nome']}")

  if input("\nDeseja sair do programa? (s/n) ") != 's':
    continue
  else:
    print("Obrigado por utilizar!")
    break
