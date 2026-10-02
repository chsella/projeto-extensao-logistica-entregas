# Projeto de Extensão

# Análise de Desempenho Logístico e Identificação de Fatores Associados a Atrasos em Entregas

**Aluna:** Ingryd Cristine Hidalgo Sella  
**RA:** 10424934  
**Curso:** Ciência de Dados

---

# 1. Introdução

A logística exerce papel fundamental nas operações de comércio
eletrônico, especialmente em relação ao processamento, transporte e
entrega dos pedidos aos consumidores.

O crescimento do comércio eletrônico aumentou a necessidade de
acompanhar o desempenho das operações logísticas por meio de
informações confiáveis e indicadores que permitam identificar possíveis
problemas no processo de entrega.

Nesse contexto, a Ciência de Dados pode ser utilizada para transformar
dados operacionais em informações capazes de auxiliar na compreensão
dos processos logísticos.

Este projeto de extensão propõe a análise de dados relacionados a
pedidos e entregas do comércio eletrônico, buscando identificar padrões
de desempenho e fatores associados à ocorrência de atrasos.

Para o desenvolvimento do projeto será utilizado o Brazilian
E-Commerce Public Dataset by Olist, uma base pública que reúne
informações sobre pedidos, clientes, vendedores, produtos, pagamentos,
avaliações e outras características relacionadas às operações de
comércio eletrônico.

---

# 2. Organização escolhida

A organização escolhida para o desenvolvimento do projeto é a Olist,
empresa brasileira de tecnologia voltada ao comércio eletrônico.

A Olist oferece soluções para empresas que desejam realizar vendas por
meio de diferentes canais digitais, estando inserida no contexto do
comércio eletrônico e das operações relacionadas ao processamento e
atendimento de pedidos.

Para este projeto, o foco será direcionado especificamente à dimensão
logística, considerando informações relacionadas ao processo de entrega
dos pedidos.

É importante destacar que o projeto não utiliza dados internos ou
confidenciais da organização. A análise será realizada utilizando uma
base de dados pública disponibilizada para estudos e análises de
comércio eletrônico.

---

# 3. Área de atuação

O projeto está inserido na área de logística e distribuição aplicada ao
comércio eletrônico.

Dentro desse contexto, o processo analisado pode ser representado
simplificadamente pelas seguintes etapas:

Pedido → Processamento → Expedição → Transporte → Entrega

Cada uma dessas etapas pode influenciar o prazo final de atendimento
do pedido.

A análise dos dados permite observar características dos pedidos e
entregas, possibilitando a construção de indicadores relacionados ao
cumprimento dos prazos.

---

# 4. Problema identificado

A ocorrência de atrasos nas entregas pode afetar a experiência dos
consumidores e também fornecer informações importantes sobre o
desempenho das operações logísticas.

Diante disso, o projeto busca responder à seguinte questão:

> Como a análise de dados pode auxiliar na identificação de fatores
> associados aos atrasos nas entregas e contribuir para o acompanhamento
> do desempenho logístico?

A partir dessa questão, serão analisadas informações relacionadas aos
pedidos, datas de processamento e entrega, localização, produtos,
vendedores e demais variáveis disponíveis no dataset.

---

# 5. Justificativa

A análise de dados aplicada à logística pode contribuir para uma melhor
compreensão do comportamento das operações de entrega.

A identificação de padrões relacionados aos atrasos permite organizar
informações que podem ser utilizadas na avaliação do desempenho
logístico.

Além disso, o projeto possibilita aplicar conhecimentos de Ciência de
Dados em uma situação relacionada ao ambiente empresarial, envolvendo
etapas de coleta, organização, tratamento, análise e visualização de
dados.

Dessa forma, o trabalho também contribui para o desenvolvimento de
competências técnicas relacionadas à utilização de dados para apoio à
tomada de decisões.

---

# 6. Objetivos

## 6.1 Objetivo geral

Analisar dados relacionados às operações de entrega para identificar
padrões de desempenho logístico e fatores associados aos atrasos,
utilizando técnicas de análise e visualização de dados.

## 6.2 Objetivos específicos

- Organizar o dataset utilizado no projeto;
- Identificar e documentar as principais variáveis;
- Realizar o tratamento dos dados;
- Analisar o tempo de entrega dos pedidos;
- Identificar ocorrências de atraso;
- Desenvolver indicadores de desempenho logístico;
- Analisar possíveis fatores associados aos atrasos;
- Desenvolver visualizações para facilitar a interpretação dos dados;
- Documentar as etapas e resultados do projeto;
- Disponibilizar o desenvolvimento do projeto por meio do GitHub.

---

# 7. Dataset utilizado

O projeto utiliza o Brazilian E-Commerce Public Dataset by Olist.

O dataset é composto por diferentes arquivos relacionados às operações
de comércio eletrônico, permitindo relacionar informações de pedidos,
clientes, vendedores, produtos, pagamentos, avaliações e localização.

Os arquivos utilizados no projeto são:

- olist_orders_dataset.csv;
- olist_customers_dataset.csv;
- olist_order_items_dataset.csv;
- olist_order_payments_dataset.csv;
- olist_order_reviews_dataset.csv;
- olist_products_dataset.csv;
- olist_sellers_dataset.csv;
- olist_geolocation_dataset.csv;
- product_category_name_translation.csv.

Os arquivos originais são armazenados no diretório:

data/raw/

A preservação dos dados originais permite manter uma cópia da base sem
alterações antes das etapas de tratamento.

---

# 8. Metadados

Os metadados apresentam informações sobre as características dos dados
utilizados no projeto.

Entre as principais informações que serão documentadas estão:

- nome da variável;
- tipo de dado;
- descrição;
- unidade de medida, quando aplicável;
- exemplo de valor;
- origem da informação.

Os metadados completos estão disponíveis no arquivo:

docs/metadados.md

---

# 9. Variáveis relacionadas às entregas

Entre as variáveis de maior interesse para o problema proposto estão as
informações relacionadas às datas do pedido e da entrega.

No arquivo de pedidos são encontradas informações como:

- identificador do pedido;
- status do pedido;
- data da realização do pedido;
- data de aprovação;
- data de entrega ao transportador;
- data de entrega ao cliente;
- data estimada de entrega.

Essas informações permitem realizar comparações entre o prazo
estimado e a entrega efetivamente realizada.

---

# 10. Indicador de atraso

Um dos principais indicadores do projeto será o atraso da entrega.

O indicador será obtido por meio da comparação entre a data efetiva de
entrega e a data estimada de entrega.

De forma simplificada:

Atraso = Data efetiva de entrega − Data estimada de entrega

Quando a entrega ocorrer após a data estimada, o pedido poderá ser
classificado como atrasado.

Quando a entrega ocorrer até a data estimada, poderá ser classificada
como realizada dentro do prazo.

Os critérios definitivos serão aplicados após a análise e tratamento dos
dados.

---

# 11. Metodologia

O desenvolvimento do projeto será dividido nas seguintes etapas:

## 11.1 Seleção dos dados

Identificação e organização do dataset público utilizado no estudo.

## 11.2 Levantamento dos metadados

Identificação das variáveis, tipos de dados, descrições e características
das tabelas.

## 11.3 Tratamento dos dados

Avaliação de valores ausentes, duplicidades, inconsistências e tipos
das variáveis.

## 11.4 Integração

Relacionamento entre as tabelas necessárias para a análise.

## 11.5 Análise exploratória

Investigação das características dos dados por meio de estatísticas
descritivas, tabelas e visualizações.

## 11.6 Criação dos indicadores

Desenvolvimento de indicadores relacionados ao tempo e ao cumprimento
dos prazos de entrega.

## 11.7 Análise dos resultados

Interpretação dos padrões encontrados e identificação de possíveis
fatores associados aos atrasos.

## 11.8 Documentação

Registro das etapas, resultados e conclusões do projeto.

---

# 12. Repositório GitHub

O projeto será desenvolvido e documentado por meio de um repositório
GitHub.

O repositório contém a estrutura necessária para organização dos dados,
documentação, códigos e resultados.

**Repositório:**

https://github.com/chsella/projeto-extensao-logistica-entregas

Estrutura principal:

- data/;
- docs/;
- notebooks/;
- resultados/;
- src/.

---

# 13. Cronograma

O cronograma do projeto está organizado de acordo com as principais
etapas de desenvolvimento.

| Atividade | Período | Responsável | Marco |
|---|---|---|---|
| Definição do tema | Semana 1 | Ingryd Cristine Hidalgo Sella | Concluído |
| Criação do repositório | Semana 1 | Ingryd Cristine Hidalgo Sella | Concluído |
| Seleção do dataset | Semana 1 | Ingryd Cristine Hidalgo Sella | Concluído |
| Organização dos dados | Semana 2 | Ingryd Cristine Hidalgo Sella | |
| Tratamento dos dados | Semana 3 | Ingryd Cristine Hidalgo Sella | |
| Análise exploratória | Semana 4 | Ingryd Cristine Hidalgo Sella | |
| Desenvolvimento dos indicadores | Semana 5 | Ingryd Cristine Hidalgo Sella | |
| Visualização dos resultados | Semana 6 | Ingryd Cristine Hidalgo Sella | |
| Documentação final | Semana 7 | Ingryd Cristine Hidalgo Sella | |
| Revisão e entrega | Semana 8 | Ingryd Cristine Hidalgo Sella | |

---

# 14. Resultados esperados

Espera-se que a análise permita compreender o comportamento das
entregas presentes no dataset e identificar padrões relacionados ao
cumprimento ou descumprimento dos prazos estimados.

Também se espera desenvolver indicadores e visualizações capazes de
facilitar a interpretação dos dados e demonstrar a aplicação de
técnicas de Ciência de Dados em um problema relacionado à logística.

---

# 15. Considerações finais

O projeto propõe a utilização de dados públicos para analisar o
desempenho de operações relacionadas à logística e às entregas no
comércio eletrônico.

Através das etapas de organização, tratamento, exploração e análise dos
dados, pretende-se transformar informações presentes no dataset em
indicadores que possibilitem compreender o comportamento das entregas.

O desenvolvimento do projeto também permite aplicar conhecimentos
adquiridos na área de Ciência de Dados em um contexto prático,
envolvendo organização de dados, análise exploratória, criação de
indicadores, visualização e documentação.

---

# 16. Referências

OLIST. Brazilian E-Commerce Public Dataset by Olist. Kaggle. Dataset
público utilizado para análise de comércio eletrônico.

KAGGLE. Brazilian E-Commerce Public Dataset by Olist. Disponível em:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

GITHUB. Projeto de Extensão – Análise de Desempenho Logístico e
Entregas. Disponível em:
https://github.com/chsella/projeto-extensao-logistica-entregas
