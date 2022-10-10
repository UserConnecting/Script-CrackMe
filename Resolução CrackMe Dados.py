"""
Feito para realização de uma etapa do desafio [CrackMe]. Consistia em descobrir a combinação correta de 8 dados, ao
fazer a exploração do código desse jogo foi possível extrair as linhas de condições que o jogo utilizava para
conceder a flag ao usuário. As condições extraídas estão nas linhas 25 e 26 desse código.

O script realiza combinações randômicas repetidamente até encontrar o resultado que cumpra cada condição.
"""


from random import randint

d = 0
d1 = randint(1, 6)
d2 = randint(1, 6)
d3 = randint(1, 6)
d4 = randint(1, 6)
d5 = randint(1, 6)
d6 = randint(1, 6)
d7 = randint(1, 6)
d8 = randint(1, 6)

print('Aguarde, testando combinações.')

while d != 1:
    if d1 + d3 + d5 + d7 == 12 and d2 + d4 + d6 + d8 == 11 and d2 * d3 * d7 == 24 and d1 * d2 * d3 * d5 == 60 \
            and d7 - d2 + d3 - d4 == 0 and d6 + d1 + d8 == 10 and d8 > 3:
        flag = f"FLAG{{{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}}}"
        print(f'{flag}')
        d += 1
    else:
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        d3 = randint(1, 6)
        d4 = randint(1, 6)
        d5 = randint(1, 6)
        d6 = randint(1, 6)
        d7 = randint(1, 6)
        d8 = randint(1, 6)
