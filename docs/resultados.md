
# Resultados e Análise do Modelo Preditivo

## 1. Caracterização da base de dados

Após a integração das bases do Olist, foi obtida uma base consolidada com **99.441 registros e 17 colunas**. Não foram identificados registros duplicados pelo identificador do pedido.

Para a análise dos prazos de entrega, foram considerados apenas os pedidos entregues que apresentavam datas válidas de entrega efetiva e estimada, totalizando **96.470 pedidos**.

## 2. Análise dos atrasos

A classificação dos pedidos foi realizada pela diferença entre a data efetiva e a data estimada de entrega.

- **Entrega no prazo ou antecipada:** diferença menor ou igual a zero.
- **Entrega atrasada:** diferença maior que zero.

Os resultados foram:

| Classificação | Quantidade | Participação |
|---|---:|---:|
| No prazo ou antecipada | 88.644 | 91,89% |
| Atrasada | 7.826 | 8,11% |
| **Total** | **96.470** | **100%** |

A taxa de atraso de 8,11% demonstra que a maior parte dos pedidos analisados foi entregue dentro do prazo estimado ou antes dele.

## 3. Desenvolvimento do modelo preditivo

Foi desenvolvido um primeiro modelo de classificação utilizando Regressão Logística.

A base foi dividida em conjuntos de treinamento e teste, mantendo a proporção das classes por meio da estratificação:

- Treinamento: 77.176 registros.
- Teste: 19.294 registros.
- Estratégia de divisão: 80% para treinamento e 20% para teste.
- Balanceamento: utilização de pesos de classe para considerar a diferença entre pedidos atrasados e não atrasados.

Foram utilizadas variáveis relacionadas às características dos pedidos e ao prazo estimado, como valor dos produtos, frete, quantidade de itens, quantidade de vendedores, prazo estimado e estado do cliente.

As datas efetivas de entrega e a quantidade de dias de atraso foram excluídas das variáveis preditoras para evitar vazamento de informações do resultado.

## 4. Métricas de avaliação

O desempenho inicial do modelo foi avaliado por meio de acurácia, precisão, recall e F1-score.

| Métrica | Resultado |
|---|---:|
| Acurácia | 63,46% |
| Precisão da classe de atraso | 13,09% |
| Recall da classe de atraso | 62,17% |
| F1-score da classe de atraso | 21,63% |

A matriz de confusão apresentou os seguintes resultados:

| Resultado real / previsto | Não atrasado | Atrasado |
|---|---:|---:|
| Não atrasado | 11.271 | 6.458 |
| Atrasado | 592 | 973 |

## 5. Interpretação dos resultados

O modelo apresentou recall de 62,17% para a classe de pedidos atrasados, indicando que conseguiu identificar parte significativa dos atrasos existentes no conjunto de teste.

Entretanto, a precisão de 13,09% demonstra que uma parcela expressiva das previsões classificadas como atraso correspondeu a pedidos que não estavam atrasados.

Esse comportamento indica a ocorrência de muitos falsos positivos. Portanto, embora o modelo consiga identificar uma parcela dos pedidos com atraso, sua capacidade de realizar previsões precisas ainda precisa ser aprimorada.

A acurácia de 63,46% também deve ser interpretada em conjunto com as demais métricas, considerando o desequilíbrio entre as classes.

## 6. Limitações identificadas

Os resultados representam uma etapa inicial do desenvolvimento do projeto. Entre as principais limitações identificadas estão:

- Baixa precisão na identificação de pedidos atrasados.
- Quantidade elevada de falsos positivos.
- Necessidade de avaliar outras técnicas de classificação.
- Necessidade de aprofundar a análise das variáveis utilizadas.
- Necessidade de verificar a disponibilidade das variáveis no momento em que a previsão seria realizada.

## 7. Próximas etapas

Para dar continuidade ao desenvolvimento, estão previstas as seguintes atividades:

1. Aprimorar a análise exploratória e a preparação dos dados.
2. Avaliar outros algoritmos de classificação.
3. Comparar os modelos utilizando as mesmas métricas.
4. Investigar estratégias para reduzir os falsos positivos.
5. Documentar os resultados comparativos.
6. Consolidar as conclusões e recomendações do projeto.

## 8. Considerações finais

Os resultados iniciais demonstram a possibilidade de utilizar técnicas de Ciência de Dados para investigar fatores associados aos atrasos nas entregas do comércio eletrônico.

A Regressão Logística constituiu uma primeira referência para a construção do modelo preditivo. Apesar de apresentar capacidade de identificação de parte dos pedidos atrasados, os resultados apontam oportunidades de melhoria, principalmente em relação à precisão.

A continuidade do projeto permitirá avaliar outros algoritmos e identificar abordagens mais adequadas ao problema estudado.
