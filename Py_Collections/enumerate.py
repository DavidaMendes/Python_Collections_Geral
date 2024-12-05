idades = [15, 87, 96, 75, 43, 24]

for i, idade in enumerate(idades, start = 1):
    print(f'{i} - {idade}')

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Guilherme', 39, 1979)
]
for nome, _, _ in usuarios: # O _ é para ignorar o resto
    print(nome) # Desenpacotamento

print(sorted(idades, reverse=True))
print(sorted(idades)) # Sort altera a variavel
