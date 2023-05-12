from funcoes import estoque
n = input('Digite o nome do produto: ')
q = int(input('Quantos produtos tem? '))
v_u = float(input('Quanto custa o produto? '))
nome, valortotal = estoque(n, q, v_u)
print(f"O valor total do produto {nome} é {valortotal}")
