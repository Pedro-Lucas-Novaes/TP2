votos_brancos = int(input("Digite o total de votos brancos: "))
votos_nulos = int(input("Digite o total de votos nulos:"))
votos_validos = int(input("Digite o total de votos validos: "))

total_eleitores = votos_brancos + votos_nulos + votos_validos
perc_brancos = (votos_brancos * 100) / total_eleitores
perc_nulos = (votos_nulos * 100) / total_eleitores
perc_validos = (votos_validos * 100) / total_eleitores


print(f"O total de eleitores é de: {total_eleitores} eleitores")
print(f"O percentual de votos brancos foi de: {perc_brancos}%")
print(f"O percentual de votos nulos foi de: {perc_nulos}%")
print(f"O percentual de votos validos foi de: {perc_validos}%")