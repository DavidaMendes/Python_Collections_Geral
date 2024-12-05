usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]


# Nesse caso o append adicionaria a LISTA, ja o extend adiciona os proprios numeros
# Copy tira uma copia

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(set(assistiram)) # Set cria um conjunto e tira os números iguais (sem ordem de importancia)

conj1 = {13, 44, 55}
conj2 = {13, 98, 78, 55}

print(conj1 | conj2)
print(conj1 & conj2)
print(conj1 - conj2) # Quem esta apenas no conjunto 1
print(44 in (conj1 - conj2)) 
print(conj1 ^ conj2) # "ou" exclusivo -- Fez apenas um dos dois cursos

usuarios = {15, 63, 75, 34, 52, 13, 17}
usuarios.add(765)
print(usuarios)
usuarios = frozenset(usuarios) # Se torna imutavel 
    
    