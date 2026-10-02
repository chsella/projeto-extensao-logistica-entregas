# Dicionário de Dados

## 1. Objetivo

Este documento apresenta a descrição das principais variáveis presentes
no dataset utilizado no projeto de extensão.

As informações são organizadas de acordo com os arquivos originais do
Brazilian E-Commerce Public Dataset by Olist.

---

# 2. Tabela de pedidos

**Arquivo:** `olist_orders_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `order_id` | Texto | Identificador único do pedido |
| `customer_id` | Texto | Identificador do cliente |
| `order_status` | Categórico | Situação do pedido |
| `order_purchase_timestamp` | Data/Hora | Data e horário da realização do pedido |
| `order_approved_at` | Data/Hora | Data e horário da aprovação do pedido |
| `order_delivered_carrier_date` | Data/Hora | Data em que o pedido foi entregue ao transportador |
| `order_delivered_customer_date` | Data/Hora | Data em que o pedido foi entregue ao cliente |
| `order_estimated_delivery_date` | Data/Hora | Data estimada para entrega ao cliente |

### Utilização no projeto

Esta tabela é uma das principais fontes de informação para a análise
do desempenho das entregas.

As datas de entrega efetiva e estimada poderão ser utilizadas para
identificar pedidos entregues após o prazo previsto.

---

# 3. Tabela de clientes

**Arquivo:** `olist_customers_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `customer_id` | Texto | Identificador do cliente |
| `customer_unique_id` | Texto | Identificador único do cliente |
| `customer_zip_code_prefix` | Numérico | Prefixo do código postal do cliente |
| `customer_city` | Texto | Cidade do cliente |
| `customer_state` | Texto | Estado do cliente |

### Utilização no projeto

Os dados de localização dos clientes poderão ser utilizados para
investigar diferenças no desempenho das entregas entre regiões.

---

# 4. Tabela de vendedores

**Arquivo:** `olist_sellers_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `seller_id` | Texto | Identificador do vendedor |
| `seller_zip_code_prefix` | Numérico | Prefixo do código postal do vendedor |
| `seller_city` | Texto | Cidade do vendedor |
| `seller_state` | Texto | Estado do vendedor |

### Utilização no projeto

As informações dos vendedores poderão ser relacionadas às informações
dos pedidos para analisar características geográficas das operações.

---

# 5. Tabela de itens dos pedidos

**Arquivo:** `olist_order_items_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `order_id` | Texto | Identificador do pedido |
| `order_item_id` | Numérico | Número sequencial do item dentro do pedido |
| `product_id` | Texto | Identificador do produto |
| `seller_id` | Texto | Identificador do vendedor |
| `shipping_limit_date` | Data/Hora | Prazo limite para envio |
| `price` | Numérico | Preço do produto |
| `freight_value` | Numérico | Valor do frete |

### Utilização no projeto

Essas informações permitem analisar características dos pedidos,
produtos, vendedores e valores relacionados ao transporte.

---

# 6. Tabela de produtos

**Arquivo:** `olist_products_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `product_id` | Texto | Identificador do produto |
| `product_category_name` | Texto | Categoria do produto |
| `product_name_lenght` | Numérico | Quantidade de caracteres do nome |
| `product_description_lenght` | Numérico | Quantidade de caracteres da descrição |
| `product_photos_qty` | Numérico | Quantidade de fotos do produto |
| `product_weight_g` | Numérico | Peso do produto em gramas |
| `product_length_cm` | Numérico | Comprimento do produto em centímetros |
| `product_height_cm` | Numérico | Altura do produto em centímetros |
| `product_width_cm` | Numérico | Largura do produto em centímetros |

### Utilização no projeto

Características dos produtos poderão ser utilizadas para investigar
possíveis relações entre características físicas dos pedidos e o
desempenho logístico.

---

# 7. Tabela de pagamentos

**Arquivo:** `olist_order_payments_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `order_id` | Texto | Identificador do pedido |
| `payment_sequential` | Numérico | Sequência do pagamento |
| `payment_type` | Categórico | Tipo de pagamento |
| `payment_installments` | Numérico | Quantidade de parcelas |
| `payment_value` | Numérico | Valor do pagamento |

### Utilização no projeto

Os dados de pagamento poderão ser utilizados para análises
complementares relacionadas às características dos pedidos.

---

# 8. Tabela de avaliações

**Arquivo:** `olist_order_reviews_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `review_id` | Texto | Identificador da avaliação |
| `order_id` | Texto | Identificador do pedido |
| `review_score` | Numérico | Nota atribuída pelo cliente |
| `review_comment_title` | Texto | Título do comentário |
| `review_comment_message` | Texto | Mensagem do comentário |
| `review_creation_date` | Data/Hora | Data de criação da avaliação |
| `review_answer_timestamp` | Data/Hora | Data e horário da resposta |

### Utilização no projeto

As avaliações poderão ser utilizadas para verificar, de forma
exploratória, possíveis relações entre experiência do cliente e
desempenho das entregas.

---

# 9. Tabela de geolocalização

**Arquivo:** `olist_geolocation_dataset.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `geolocation_zip_code_prefix` | Numérico | Prefixo do código postal |
| `geolocation_lat` | Numérico | Latitude |
| `geolocation_lng` | Numérico | Longitude |
| `geolocation_city` | Texto | Cidade |
| `geolocation_state` | Texto | Estado |

### Utilização no projeto

Os dados geográficos poderão ser utilizados para análises relacionadas
à distribuição espacial dos clientes e vendedores.

---

# 10. Tradução das categorias

**Arquivo:** `product_category_name_translation.csv`

| Variável | Tipo | Descrição |
|---|---|---|
| `product_category_name` | Texto | Nome da categoria em português |
| `product_category_name_english` | Texto | Nome da categoria em inglês |

### Utilização no projeto

A tabela permite relacionar os nomes das categorias de produtos em
português e inglês.

---

# 11. Variáveis prioritárias para a análise logística

Embora o dataset possua diversas informações, o projeto dará
prioridade às variáveis relacionadas diretamente ao processo de
entrega.

As principais são:

- `order_purchase_timestamp`;
- `order_delivered_carrier_date`;
- `order_delivered_customer_date`;
- `order_estimated_delivery_date`;
- `customer_city`;
- `customer_state`;
- `seller_city`;
- `seller_state`;
- `shipping_limit_date`;
- `freight_value`.

Essas variáveis serão utilizadas, conforme a disponibilidade e
qualidade dos registros, para construir indicadores e realizar análises
sobre o desempenho das entregas.

---

# 12. Novas variáveis

Durante o tratamento dos dados poderão ser criadas novas variáveis
derivadas das informações originais.

Entre elas:

### Dias de entrega

Diferença entre a data de compra e a data efetiva de entrega.

### Dias de atraso

Diferença entre a data efetiva de entrega e a data estimada.

### Status do prazo

Classificação do pedido como:

- Dentro do prazo;
- Atrasado.

As regras definitivas de classificação serão documentadas durante a
etapa de tratamento dos dados.
