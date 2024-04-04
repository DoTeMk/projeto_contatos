def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):  
  contato = {"contato": nome_contato,"telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)  
  print(f"O contato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de Contatos:")
  for indice,contato in enumerate(contatos, start=1):
    status = "✓" if contato["favorito"] else " "    
    print(f"{indice}. [{status}] - Nome: {nome_contato}  Telefone: {telefone_contato}  Email: {email_contato}")
  return

def editar_contato(contatos, indice_contato_ajustado, novo_nome_contato, novo_telefone_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
    contatos[indice_contato_ajustado]["email"] = novo_email_contato
    print(f"Contato {indice_contato} atualizado para Nome: {novo_nome_contato}  Telefone: {novo_telefone_contato}  Email: {novo_email_contato} com sucesso!")
  else:
    print("Indice de contato inválido")  
    return
      
def marcar_como_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = True
  print(f"Contato {indice_contato} marcado como favorito!")
  return

def ver_lista_favoritos(contatos):  
  for indice,contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      status = "✓" if contato["favorito"] else " "      
      print(f"{indice}. [{status}] - Nome: {nome_contato}  Telefone: {telefone_contato}  Email: {email_contato}")
  return

def apagar_dos_favoritos(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if contatos[indice_contato_ajustado]["favorito"]: 
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} apagado dos favoritos!")
  else:
    print("Contato não está adicionado como favorito!")    
  return

def apagar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  for contato in contatos:
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
      contatos.remove(contato)
      print(f"Contato {indice_contato} removido com Sucesso")
    else:
      print("Indice errado")
  
contatos = []
while True:
  print("\nMenu de Opções do App:")
  print("1. Adicionar Contato")
  print("2. Ver contatos")
  print("3. Editar um contato")
  print("4. Marcar contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Apagar contato dos favoritos")
  print("7. Apagar um contato")
  print("8. Sair")

  escolha = input("Escolha a oppção desejada: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone_contato = input("Digite o telefone do contato: ")
    email_contato = input("Digite o email do contato: ")
    adicionar_contato(contatos,nome_contato,telefone_contato, email_contato)

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que você quer atualizar:  ")
    novo_nome_contato = input("Digite o novo nome do contato: ")
    novo_telefone_contato = input("Digite o novo telefone do contato: ")
    novo_email_contato = input("Digite o novo email do contato: ")
    editar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)

  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que quer marcar como favorito: ")
    marcar_como_favorito(contatos,indice_contato)
    
  elif escolha == "5":
    ver_lista_favoritos(contatos) 

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que quer apagar dos favoritos: ")
    apagar_dos_favoritos(contatos,indice_contato)

  elif escolha == "7":
    ver_contatos(contatos)
    indice_contato = input("Digite o numero do contato que você quer remover: ")
    apagar_contato(contatos,indice_contato)

  if escolha == "8":
    break

print("Aplicativo Finalizado")