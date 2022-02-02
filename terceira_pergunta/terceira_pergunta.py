'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

with open('dados.json', 'r', encoding='utf-8-sig') as file:
    dados = json.loads(file.read())

listaDiaLucroForaMedia = []
listaGeral = []
listaValores = []



for ind in dados:
    
    if ind['valor'] <= 0:
        pass
    else:
        listaGeral.append(ind)
        listaValores.append(ind['valor'])
    
    menorValorOcorrido= min(listaValores)
    maiorValorOcorrido= max(listaValores)
    numeroDias = len(listaGeral)
    mediaMensal = sum(listaValores)/numeroDias

    if ind['valor'] > mediaMensal:
        listaDiaLucroForaMedia.append(ind)


print(f'''RELATORIO:\n\nO menor valor de faturamento ocorrido em um dia do mês: R${menorValorOcorrido}\n
O maior valor de faturamento ocorrido em um dia do mês: R${maiorValorOcorrido}\n
Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {len(listaDiaLucroForaMedia)}
''')
