# Indicadores Logísticos

## 1. Objetivo

Os indicadores logísticos serão utilizados para avaliar o desempenho
das entregas presentes no dataset e identificar possíveis padrões
relacionados ao cumprimento dos prazos.

A análise terá como foco principal a comparação entre as datas previstas
e as datas efetivamente registradas para as entregas.

---

# 2. Principais variáveis utilizadas

As principais variáveis utilizadas na construção dos indicadores serão:

| Variável | Arquivo | Finalidade |
|---|---|---|
| `order_purchase_timestamp` | pedidos | Identificar a data de realização do pedido |
| `order_delivered_carrier_date` | pedidos | Identificar quando o pedido foi entregue ao transportador |
| `order_delivered_customer_date` | pedidos | Identificar quando o pedido foi entregue ao cliente |
| `order_estimated_delivery_date` | pedidos | Identificar a data estimada para entrega |
| `order_status` | pedidos | Identificar a situação do pedido |
| `customer_state` | clientes | Analisar a localização do cliente |
| `seller_state` | vendedores | Analisar a localização do vendedor |
| `freight_value` | itens dos pedidos | Analisar o valor do frete |
| `price` | itens dos pedidos | Analisar o valor do produto |

---

# 3. Dias de entrega

O indicador de dias de entrega representa o período entre a realização
do pedido e a entrega efetiva ao cliente.

### Fórmula

**Dias de entrega = Data de entrega ao cliente − Data da compra**

Esse indicador permitirá observar o tempo necessário para que os pedidos
sejam entregues aos consumidores.

---

# 4. Dias de atraso

O indicador de dias de atraso será calculado comparando a data efetiva
de entrega com a data estimada para a entrega.

### Fórmula

**Dias de atraso = Data de entrega ao cliente − Data estimada de entrega**

Valores positivos indicarão que a entrega ocorreu após a data estimada.

Valores iguais ou inferiores a zero indicarão que a entrega ocorreu até
a data estimada.

---

# 5. Classificação do prazo

A partir do indicador de dias de atraso, os pedidos poderão ser
classificados em duas categorias principais:

| Classificação | Critério |
|---|---|
| Dentro do prazo | Entrega realizada até a data estimada |
| Atrasado | Entrega realizada após a data estimada |

Essa classificação será utilizada nas análises posteriores.

---

# 6. Taxa de entregas atrasadas

Será calculada a proporção de pedidos entregues após a data estimada.

### Fórmula

**Taxa de atraso = Número de pedidos atrasados / Número de pedidos analisados × 100**

Esse indicador permitirá observar a participação dos pedidos que não
cumpriram o prazo estimado.

---

# 7. Tempo médio de entrega

Também será analisado o tempo médio necessário para realizar as
entregas.

### Fórmula

**Tempo médio de entrega = Soma dos dias de entrega / Número de pedidos entregues**

Esse indicador permitirá comparar diferentes grupos de pedidos.

---

# 8. Análise por localização

Os indicadores poderão ser analisados de acordo com a localização dos
clientes e vendedores.

Entre as possibilidades de análise estão:

- Estado do cliente;
- Estado do vendedor;
- Cidade do cliente;
- Cidade do vendedor;
- Relação entre localização do vendedor e cliente.

O objetivo será verificar se existem diferenças nos padrões de entrega
entre diferentes regiões.

---

# 9. Análise do frete

O valor do frete será utilizado como uma variável complementar da
análise.

Será investigada a possível relação entre:

- valor do frete;
- tempo de entrega;
- ocorrência de atraso;
- localização do cliente;
- localização do vendedor.

Essa análise será exploratória e não terá como objetivo estabelecer
causalidade apenas a partir das relações observadas nos dados.

---

# 10. Análise dos vendedores

Os dados dos vendedores poderão ser relacionados aos pedidos para
identificar padrões de desempenho.

Entre os indicadores que poderão ser observados estão:

- quantidade de pedidos;
- tempo médio de entrega;
- quantidade de pedidos atrasados;
- taxa de atraso;
- localização do vendedor.

A análise será realizada considerando somente os dados disponíveis no
dataset.

---

# 11. Análise temporal

As datas dos pedidos e entregas também poderão ser utilizadas para
identificar variações ao longo do período disponível na base.

Poderão ser analisados:

- volume de pedidos ao longo do tempo;
- tempo médio de entrega;
- quantidade de atrasos;
- taxa de atraso;
- comportamento das entregas por período.

---

# 12. Visualizações previstas

Para facilitar a interpretação dos resultados, poderão ser utilizadas
visualizações como:

- gráficos de barras;
- gráficos de linhas;
- histogramas;
- gráficos de distribuição;
- tabelas comparativas;
- mapas, caso os dados geográficos sejam utilizados.

As visualizações serão documentadas posteriormente no projeto.

---

# 13. Cuidados na interpretação

Os indicadores serão utilizados para descrever padrões observados no
dataset.

A existência de associação entre duas variáveis não será interpretada
automaticamente como relação de causa e efeito.

Também serão considerados os registros ausentes, inconsistentes ou que
não possuam informações suficientes para o cálculo dos indicadores.

---

# 14. Resultado esperado

Espera-se que os indicadores permitam construir uma visão estruturada
do desempenho das entregas e apoiar a identificação de padrões
relacionados aos atrasos.

Os resultados serão apresentados posteriormente por meio de tabelas,
gráficos e análises descritivas.
