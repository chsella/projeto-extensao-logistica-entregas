Projeto de Extensão
Análise de Desempenho Logístico e Identificação de Fatores Associados a Atrasos em Entregas
Aluna: Ingryd Cristine Hidalgo Sella
RA: 10424934
Curso: Ciência de Dados
1. Introdução
A logística exerce papel fundamental nas operações de comércio eletrônico, especialmente em relação ao processamento, transporte e entrega dos pedidos aos consumidores.

O crescimento do comércio eletrônico aumentou a necessidade de acompanhar o desempenho das operações logísticas por meio de informações confiáveis e indicadores que permitam identificar possíveis problemas no processo de entrega.

Nesse contexto, a Ciência de Dados pode ser utilizada para transformar dados operacionais em informações capazes de auxiliar na compreensão dos processos logísticos.

Este projeto de extensão propõe a análise de dados relacionados a pedidos e entregas do comércio eletrônico, buscando identificar padrões de desempenho e fatores associados à ocorrência de atrasos.

Para o desenvolvimento do projeto será utilizado o Brazilian E-Commerce Public Dataset by Olist, uma base pública que reúne informações sobre pedidos, clientes, vendedores, produtos, pagamentos, avaliações e outras características relacionadas às operações de comércio eletrônico.
2. Organização escolhida
A organização escolhida para o desenvolvimento do projeto é a Olist, empresa brasileira de tecnologia voltada ao comércio eletrônico.

A Olist oferece soluções para empresas que desejam realizar vendas por meio de diferentes canais digitais, estando inserida no contexto do comércio eletrônico e das operações relacionadas ao processamento e atendimento de pedidos.

Para este projeto, o foco será direcionado especificamente à dimensão logística, considerando informações relacionadas ao processo de entrega dos pedidos.

É importante destacar que o projeto não utiliza dados internos ou confidenciais da organização. A análise será realizada utilizando uma base de dados pública disponibilizada para estudos e análises de comércio eletrônico.
3. Área de atuação
O projeto está inserido na área de logística e distribuição aplicada ao comércio eletrônico.

Dentro desse contexto, o processo analisado pode ser representado simplificadamente pelas seguintes etapas:

Pedido → Processamento → Expedição → Transporte → Entrega

Cada uma dessas etapas pode influenciar o prazo final de atendimento do pedido.

A análise dos dados permite observar características dos pedidos e entregas, possibilitando a construção de indicadores relacionados ao cumprimento dos prazos.
4. Problema identificado
A ocorrência de atrasos nas entregas pode afetar a experiência dos consumidores e também fornecer informações importantes sobre o desempenho das operações logísticas.

Diante disso, o projeto busca responder à seguinte questão:
Como a análise de dados pode auxiliar na identificação de fatores associados aos atrasos nas entregas e contribuir para o acompanhamento do desempenho logístico?

A partir dessa questão, serão analisadas informações relacionadas aos pedidos, datas de processamento e entrega, localização, produtos, vendedores e demais variáveis disponíveis no dataset.
5. Justificativa
A análise de dados aplicada à logística pode contribuir para uma melhor compreensão do comportamento das operações de entrega.

A identificação de padrões relacionados aos atrasos permite organizar informações que podem ser utilizadas na avaliação do desempenho logístico.

Além disso, o projeto possibilita aplicar conhecimentos de Ciência de Dados em uma situação relacionada ao ambiente empresarial, envolvendo etapas de coleta, organização, tratamento, análise e visualização de dados.

Dessa forma, o trabalho também contribui para o desenvolvimento de competências técnicas relacionadas à utilização de dados para apoio à tomada de decisões.
6. Objetivos
6.1 Objetivo geral
Analisar dados relacionados às operações de entrega para identificar padrões de desempenho logístico e fatores associados aos atrasos, utilizando técnicas de análise e visualização de dados.
6.2 Objetivos específicos
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
7. Dataset utilizado
O projeto utiliza o Brazilian E-Commerce Public Dataset by Olist.

O dataset é composto por diferentes arquivos relacionados às operações de comércio eletrônico, permitindo relacionar informações de pedidos, clientes, vendedores, produtos, pagamentos, avaliações e localização.

Os arquivos considerados no projeto são:
- olist_orders_dataset.csv;
- olist_customers_dataset.csv;
- olist_order_items_dataset.csv;
- olist_order_payments_dataset.csv;
- olist_order_reviews_dataset.csv;
- olist_products_dataset.csv;
- olist_sellers_dataset.csv;
- olist_geolocation_dataset.csv;
- product_category_name_translation.csv.
Para a análise exploratória e o primeiro modelo descritos neste documento, foram carregados e integrados os arquivos de pedidos, clientes, itens dos pedidos e pagamentos. Os demais arquivos estão listados como fontes disponíveis para possíveis extensões da análise; sua inclusão nas etapas já realizadas não é presumida.

Os arquivos originais são armazenados no diretório:

data/raw/

A preservação dos dados originais permite manter uma cópia da base sem alterações antes das etapas de tratamento.
8. Metadados
Os metadados apresentam informações sobre as características dos dados utilizados no projeto.

Entre as principais informações documentadas estão:
- nome da variável;
- tipo de dado;
- descrição;
- unidade de medida, quando aplicável;
- exemplo de valor;
- origem da informação.
Os metadados do projeto estão disponíveis no arquivo:

docs/metadados.md
9. Variáveis relacionadas às entregas
Entre as variáveis de maior interesse para o problema proposto estão as informações relacionadas às datas do pedido e da entrega.

No arquivo de pedidos são encontradas informações como:
- identificador do pedido;
- status do pedido;
- data da realização do pedido;
- data de aprovação;
- data de entrega ao transportador;
- data de entrega ao cliente;
- data estimada de entrega.
As tabelas complementares acrescentam informações como estado e cidade do cliente, quantidade de itens, valor dos produtos, valor do frete e dados agregados de pagamento.

Essas informações permitem comparar a data estimada com a data efetiva de entrega e analisar características dos pedidos que poderão estar associadas aos atrasos.
10. Indicador de atraso
Um dos principais indicadores do projeto é o atraso da entrega.

O indicador foi obtido por meio da comparação entre a data efetiva de entrega ao cliente e a data estimada de entrega.

Diferença de entrega = Data efetiva de entrega − Data estimada de entrega

Quando a entrega ocorre após a data estimada, o pedido é classificado como atrasado. Quando ocorre até a data estimada, é classificado como entregue no prazo ou antecipadamente.

Para o cálculo, foram considerados apenas pedidos com status delivered e com as datas efetiva e estimada de entrega disponíveis. A variável binária atrasado recebeu valor 1 quando a diferença foi maior que zero e valor 0 nos demais casos válidos.
11. Metodologia
O desenvolvimento do projeto foi organizado em etapas de seleção, preparação, integração, exploração e modelagem dos dados.
11.1 Seleção dos dados
Foi selecionado o dataset público da Olist. Para as análises realizadas até o momento, foram carregadas as tabelas de pedidos, clientes, itens dos pedidos e pagamentos a partir dos arquivos CSV armazenados no repositório do projeto.
11.2 Levantamento dos metadados
Foram identificadas as variáveis necessárias para a análise, incluindo identificadores de pedidos e clientes, status dos pedidos, datas de compra e entrega, localização dos clientes, valores dos itens e informações de pagamento.
11.3 Tratamento dos dados
As colunas de data foram convertidas para o formato de data e hora. Foram verificados os valores ausentes e os identificadores duplicados. Os pedidos sem datas válidas para a comparação de entrega não foram utilizados no cálculo do indicador de atraso.
11.4 Integração das tabelas
As tabelas foram integradas pelo identificador do pedido ou do cliente, conforme a relação entre elas. Como um pedido pode conter vários itens e vários registros de pagamento, essas tabelas foram previamente agregadas por pedido.

A tabela de itens foi resumida por meio da quantidade de itens, soma dos valores dos produtos, soma dos valores de frete e quantidade de vendedores distintos. A tabela de pagamentos foi resumida pela soma dos valores pagos, maior número de parcelas e quantidade de registros de pagamento.

Após a integração, a base apresentou 99.441 registros e 17 colunas, sem identificadores de pedido duplicados.
11.5 Análise exploratória
Foi realizada a contagem dos pedidos entregues com datas válidas e a classificação dos pedidos conforme o cumprimento do prazo estimado. Também foram observadas as dimensões da base integrada e a presença de valores ausentes.
11.6 Criação dos indicadores
Foi criada a variável dias_atraso, calculada pela diferença entre a data efetiva e a data estimada de entrega, expressa em dias. A variável atrasado foi definida como 1 quando dias_atraso era maior que zero e como 0 quando a entrega ocorreu no prazo ou antecipadamente.
11.7 Preparação das variáveis para modelagem
Para o primeiro modelo, foram utilizadas variáveis relacionadas ao valor dos produtos, valor do frete, quantidade de itens, quantidade de vendedores, prazo estimado e estado do cliente. O prazo estimado foi calculado pela diferença entre a data estimada de entrega e a data da compra.

As variáveis numéricas foram preparadas com imputação pela mediana e padronização. A variável categórica de estado foi tratada por imputação da categoria mais frequente e codificação one-hot. O pré-processamento foi realizado em um pipeline ajustado com os dados de treinamento.

As variáveis de data efetiva de entrega e os dias de atraso não foram usados como entradas do modelo, pois são informações necessárias para definir o resultado que se deseja prever. As variáveis de pagamento e a cidade do cliente também não foram utilizadas no primeiro modelo.
11.8 Modelagem preditiva
Foi desenvolvido um modelo inicial de Regressão Logística para classificar os pedidos entre atrasados e não atrasados. A base foi dividida em 80% para treinamento e 20% para teste, com estratificação para preservar aproximadamente a proporção das classes.

Foram utilizados 77.176 registros para treinamento e 19.294 registros para teste. O parâmetro class_weight="balanced" foi empregado para atribuir pesos às classes de acordo com sua frequência no conjunto de treinamento.
11.9 Avaliação do modelo
O desempenho foi avaliado por meio da acurácia, precisão, recall, F1-score e matriz de confusão. Essas métricas permitem avaliar tanto o desempenho geral quanto a capacidade de identificar pedidos atrasados e a quantidade de previsões incorretas.
11.10 Documentação
As etapas realizadas, os resultados obtidos e as limitações observadas são registrados na documentação do projeto e no repositório GitHub.
12. Repositório GitHub
O projeto é desenvolvido e documentado por meio de um repositório GitHub.

O repositório organiza os dados, a documentação, os notebooks e os resultados produzidos durante o desenvolvimento.

Repositório:

https://github.com/chsella/projeto-extensao-logistica-entregas

Estrutura principal:
- data/;
- docs/;
- notebooks/;
- resultados/;
- src/.
13. Cronograma
O cronograma está organizado de acordo com as principais etapas do projeto. O status das atividades deve ser atualizado conforme a execução efetiva.
Atividade	Período	Responsável	Marco
Definição do tema	Semana 1	Ingryd Cristine Hidalgo Sella	Concluído
Criação do repositório	Semana 1	Ingryd Cristine Hidalgo Sella	Concluído
Seleção do dataset	Semana 1	Ingryd Cristine Hidalgo Sella	Concluído
Organização e carregamento dos dados	Semana 2	Ingryd Cristine Hidalgo Sella	Concluído
Integração das tabelas utilizadas	Semana 2	Ingryd Cristine Hidalgo Sella	Concluído
Tratamento e criação do indicador de atraso	Semana 3	Ingryd Cristine Hidalgo Sella	Concluído
Análise exploratória inicial	Semana 4	Ingryd Cristine Hidalgo Sella	Concluído
Desenvolvimento do primeiro modelo	Semana 5	Ingryd Cristine Hidalgo Sella	Concluído
Comparação de modelos e aprimoramentos	Semana 6	Ingryd Cristine Hidalgo Sella	Pendente
Documentação final e visualizações adicionais	Semana 7	Ingryd Cristine Hidalgo Sella	Em andamento
Revisão e entrega	Semana 8	Ingryd Cristine Hidalgo Sella	Pendente


14. Resultados e avaliação do modelo
14.1 Resultados da análise exploratória
A integração das tabelas de pedidos, clientes, itens e pagamentos resultou em uma base com 99.441 registros e 17 colunas, sem duplicação de identificadores de pedidos.

Para a análise de atrasos, foram considerados 96.470 pedidos com status de entrega concluída e datas efetiva e estimada disponíveis. Desse total, 88.644 foram entregues no prazo ou antecipadamente e 7.826 apresentaram atraso, correspondendo a uma taxa de atraso de 8,11%.

A taxa de atraso indica que a classe de pedidos atrasados é minoritária no conjunto analisado. Essa característica foi considerada na escolha das métricas de avaliação do modelo.
14.2 Resultados da Regressão Logística
O primeiro modelo de Regressão Logística foi treinado com 77.176 registros e avaliado em um conjunto de teste com 19.294 registros. Os resultados obtidos no conjunto de teste foram:
Métrica	Resultado
Acurácia	63,46%
Precisão para a classe de atrasos	13,09%
Recall para a classe de atrasos	62,17%
F1-score para a classe de atrasos	21,63%


A matriz de confusão foi:
Resultado real	Previsto no prazo ou antecipado	Previsto como atrasado
No prazo ou antecipado	11.271	6.458
Atrasado	592	973


Assim, o modelo identificou corretamente 973 pedidos atrasados e deixou de identificar 592 atrasos. Também classificou incorretamente 6.458 pedidos não atrasados como atrasados.
14.3 Interpretação dos resultados
O recall de 62,17% indica que o modelo identificou aproximadamente 62% dos atrasos reais presentes no conjunto de teste. Entretanto, a precisão de 13,09% demonstra que apenas uma parcela dos pedidos sinalizados pelo modelo como atrasados realmente estava atrasada.

A acurácia de 63,46% deve ser interpretada em conjunto com as demais métricas, considerando o desequilíbrio entre as classes. A precisão reduzida e o número de falsos positivos indicam que o modelo ainda precisa ser aprimorado antes de ser considerado útil para apoiar decisões operacionais.

Os resultados constituem uma linha de base para comparações futuras. A análise não demonstra relações causais entre as características dos pedidos e os atrasos; ela avalia o desempenho preditivo inicial com as variáveis selecionadas.
14.4 Limitações e continuidade
O modelo apresentado é uma primeira versão e utiliza um conjunto limitado de variáveis. A próxima etapa poderá envolver a comparação com outros classificadores, a avaliação de diferentes configurações e o estudo de estratégias para reduzir falsos positivos sem perder a capacidade de identificar atrasos.

Também será importante confirmar que todas as variáveis usadas como entradas estariam disponíveis no momento real em que a previsão seria feita. A data estimada de entrega foi considerada disponível no momento da compra, mas essa hipótese deve ser compatível com o processo que se pretende representar.

Os resultados obtidos são referentes ao conjunto de teste desta execução e devem ser interpretados como resultados preliminares, não como garantia de desempenho em operações futuras.
15. Considerações finais
O projeto aplica técnicas de Ciência de Dados à análise de entregas no comércio eletrônico, utilizando dados públicos da Olist. Até o momento, foram realizadas a integração das principais tabelas, a identificação dos pedidos com datas válidas, a criação do indicador de atraso e a construção de um primeiro modelo de classificação.

A análise exploratória identificou 7.826 pedidos atrasados entre 96.470 entregas válidas, correspondendo a 8,11% de atrasos. O modelo inicial de Regressão Logística apresentou recall de 62,17% para a classe de atrasos, mas precisão de 13,09%, indicando a necessidade de melhorias para reduzir previsões incorretas.

Como continuidade, serão avaliadas alternativas de modelagem e realizadas novas análises para compreender melhor os fatores associados aos atrasos. Dessa forma, o projeto demonstra a aplicação prática de organização, tratamento, análise e modelagem de dados a um problema de logística, reconhecendo as limitações dos resultados preliminares.
16. Referências
OLIST. Brazilian E-Commerce Public Dataset by Olist. Kaggle. Dataset público utilizado para análise de comércio eletrônico.

KAGGLE. Brazilian E-Commerce Public Dataset by Olist. Disponível em: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

GITHUB. Projeto de Extensão – Análise de Desempenho Logístico e Identificação de Fatores Associados a Atrasos em Entregas. Disponível em: https://github.com/chsella/projeto-extensao-logistica-entregas
