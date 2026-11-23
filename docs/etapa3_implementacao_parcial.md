
# Etapa 3 – Implementação Parcial
## Análise de Desempenho Logístico e Identificação de Fatores Associados a Atrasos em Entregas

**Aluna:** Ingryd Cristine Hidalgo Sella  
**RA:** 10424934  
**Curso:** Ciência de Dados  
**Instituição:** Universidade Presbiteriana Mackenzie  
**Data de referência:** 26/10/2026  
**Checkpoint:** 05/10/2026

---

# 1. Análise Exploratória e Pré-processamento dos Dados

## 1.1 Base de dados utilizada

O projeto utiliza o Brazilian E-Commerce Public Dataset by Olist, conjunto de dados público que reúne informações sobre pedidos realizados em uma plataforma de comércio eletrônico brasileira.

Foram utilizadas as tabelas referentes a:

- Pedidos (`olist_orders_dataset`);
- Clientes (`olist_customers_dataset`);
- Itens dos pedidos (`olist_order_items_dataset`);
- Pagamentos (`olist_order_payments_dataset`).

A análise considera informações relacionadas à realização dos pedidos, aos valores dos produtos e fretes, à localização dos clientes e às datas previstas e efetivas de entrega.

## 1.2 Qualidade e limitações dos dados

A base original de pedidos contém 99.441 registros.

Após a seleção dos pedidos com status de entrega concluída e datas válidas para comparação entre a entrega efetiva e a estimada, foram considerados 96.470 pedidos na análise do indicador de atraso.

Foram identificados dados ausentes em algumas variáveis, especialmente nas informações de datas de aprovação, despacho e entrega.

Como recorte metodológico, pedidos sem as datas necessárias para calcular o atraso não foram considerados na construção do indicador.

Uma limitação importante é que os dados representam um conjunto histórico, não necessariamente refletindo as condições logísticas atuais.

## 1.3 Indicador de atraso

O indicador foi construído pela diferença entre a data efetiva de entrega ao cliente e a data estimada de entrega.

- Resultado positivo: entrega atrasada.
- Resultado igual ou negativo: entrega dentro do prazo ou antecipada.

Na base analisada, foram identificados:

| Situação | Quantidade |
|---|---:|
| Dentro do prazo ou antecipado | 88.644 |
| Atrasado | 7.826 |
| Total | 96.470 |

A proporção de pedidos atrasados corresponde a aproximadamente 8,11% dos registros válidos.

## 1.4 Pré-processamento

As atividades de preparação dos dados envolveram:

- Conversão das colunas de datas para o formato apropriado;
- Seleção de pedidos com status de entrega concluída;
- Verificação de registros com informações ausentes;
- Integração das informações de pedidos, clientes e itens;
- Consolidação de informações relacionadas aos produtos e fretes por pedido;
- Construção do indicador binário de atraso;
- Seleção das variáveis utilizadas no modelo preditivo.

Para a modelagem, foram consideradas variáveis numéricas e categóricas.

As variáveis numéricas receberam imputação pela mediana e padronização. A variável categórica de estado do cliente recebeu imputação pela categoria mais frequente e codificação One-Hot Encoding.

## 1.5 Resultados da análise exploratória

A análise exploratória permitiu observar a distribuição dos pedidos entre entregas realizadas dentro do prazo e entregas atrasadas.

Também foram consideradas informações sobre tempo de entrega, dias de atraso e distribuição geográfica dos pedidos.

A proporção relativamente pequena de entregas atrasadas demonstra um desequilíbrio entre as classes, aspecto considerado posteriormente na escolha e configuração do modelo preditivo.

---

# 2. Modelo Base

## 2.1 Método aplicado

Como primeiro modelo preditivo, foi utilizada a Regressão Logística, método de classificação supervisionada adequado à identificação de duas categorias: pedidos atrasados e pedidos entregues dentro do prazo ou antecipadamente.

A variável-alvo foi definida como:

- 0: dentro do prazo ou antecipado;
- 1: atrasado.

## 2.2 Variáveis utilizadas

Foram selecionadas as seguintes variáveis de entrada:

| Variável | Descrição |
|---|---|
| valor_produtos | Valor total dos produtos do pedido |
| valor_frete | Valor total do frete |
| quantidade_itens | Quantidade de itens do pedido |
| quantidade_vendedores | Quantidade de vendedores envolvidos |
| prazo_estimado_dias | Prazo estimado para entrega |
| customer_state | Estado do cliente |

As datas efetivas de entrega e o número de dias de atraso não foram utilizados como variáveis de entrada, evitando o uso direto de informações que compõem o resultado que se deseja prever.

## 2.3 Configuração do treinamento

A base foi dividida em conjuntos de treinamento e teste, utilizando a proporção de 80% e 20%, respectivamente.

Foram adotadas as seguintes configurações:

- Divisão estratificada das classes;
- `random_state=42`;
- Balanceamento de classes com `class_weight="balanced"`;
- Imputação de valores ausentes;
- Padronização das variáveis numéricas;
- Codificação das variáveis categóricas;
- Utilização de Pipeline e ColumnTransformer.

## 2.4 Resultados do modelo base

O modelo apresentou os seguintes resultados:

| Métrica | Resultado |
|---|---:|
| Acurácia | 63,46% |
| Precisão | 13,09% |
| Recall | 62,17% |
| F1-score | 21,63% |

### Matriz de confusão

| Classe real / prevista | Previsto no prazo | Previsto atrasado |
|---|---:|---:|
| Real no prazo | 11.271 | 6.458 |
| Real atrasado | 592 | 973 |

## 2.5 Interpretação dos resultados

Os resultados indicam que o modelo conseguiu identificar aproximadamente 62% dos pedidos que realmente apresentaram atraso.

Entretanto, a precisão de 13,09% demonstra que uma parcela significativa dos pedidos classificados como atrasados não correspondeu a atrasos efetivos.

A acurácia de 63,46%, isoladamente, não representa adequadamente o desempenho do modelo, principalmente devido ao desequilíbrio entre as classes.

Portanto, a Regressão Logística foi estabelecida como modelo inicial de referência, sendo necessário avaliar melhorias e comparar seu desempenho com outros algoritmos na continuidade do projeto.

---

# 3. Cronograma Atualizado

O cronograma foi organizado considerando as atividades concluídas, as atividades em andamento e as etapas necessárias para a entrega final.

| Atividade | Situação |
|---|---|
| Definição do problema e dos objetivos | Concluída |
| Identificação e seleção da base de dados | Concluída |
| Análise exploratória inicial | Desenvolvida |
| Integração e preparação dos dados | Desenvolvida |
| Construção do indicador de atraso | Concluída |
| Implementação da Regressão Logística | Concluída |
| Avaliação do modelo base | Concluída |
| Revisão e complementação da análise exploratória | Em andamento |
| Comparação com outros modelos | Pendente |
| Ajuste e otimização dos modelos | Pendente |
| Consolidação dos resultados e visualizações | Em andamento |
| Revisão da documentação | Em andamento |
| Preparação da entrega final | Pendente |

As atividades pendentes estão concentradas no aprimoramento da análise, na comparação entre modelos e na consolidação dos resultados.

---

# 4. Atualização do Pipeline Proposto

O pipeline foi estruturado para organizar as etapas de desenvolvimento da solução analítica.

## 4.1 Fluxo de processamento

1. **Coleta de dados:** obtenção das tabelas públicas disponibilizadas pela Olist.
2. **Inspeção inicial:** verificação da estrutura, qualidade e consistência dos arquivos.
3. **Pré-processamento:** tratamento de dados ausentes, conversão de datas e organização das variáveis.
4. **Integração:** combinação das informações de pedidos, clientes e itens.
5. **Análise exploratória:** investigação dos padrões de entrega e identificação de possíveis fatores associados aos atrasos.
6. **Construção da variável-alvo:** classificação dos pedidos entre atrasados e não atrasados.
7. **Preparação para modelagem:** seleção das variáveis, imputação, padronização e codificação.
8. **Treinamento:** aplicação do modelo base de Regressão Logística.
9. **Avaliação:** análise das métricas de classificação e da matriz de confusão.
10. **Aprimoramento:** comparação com outros algoritmos e avaliação de estratégias para melhorar os resultados.

## 4.2 Melhorias previstas

Para a continuidade do projeto, estão previstas:

- Avaliação de outros algoritmos de classificação;
- Comparação entre os resultados dos modelos;
- Investigação de estratégias para reduzir falsos positivos;
- Análise da importância das variáveis;
- Aprimoramento das visualizações;
- Consolidação dos resultados e documentação técnica.

O pipeline permanece em evolução, permitindo ajustes conforme os resultados das próximas etapas.

---

# 5. Considerações Finais da Etapa

A implementação parcial permitiu avançar da análise inicial dos dados para a construção de um primeiro modelo preditivo de atrasos em entregas.

A análise exploratória possibilitou compreender a distribuição dos pedidos e estabelecer um indicador objetivo de atraso. O pré-processamento organizou as informações necessárias para a modelagem, enquanto a Regressão Logística forneceu uma primeira referência quantitativa para avaliação da solução.

Apesar dos resultados iniciais, a baixa precisão demonstra a necessidade de aprimoramento do modelo e de novas avaliações.

As próximas atividades estarão concentradas na comparação de algoritmos, no refinamento do pipeline e na consolidação dos resultados para a entrega final.

---

**Repositório do projeto:**  
https://github.com/chsella/projeto-extensao-logistica-entregas
