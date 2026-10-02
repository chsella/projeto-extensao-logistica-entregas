import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

# ==========================================
# 1. CARREGAMENTO DOS DADOS
# ==========================================

DATA_PATH = '../data/raw/'

orders = pd.read_csv(
    DATA_PATH + 'olist_orders_dataset.csv'
)

customers = pd.read_csv(
    DATA_PATH + 'olist_customers_dataset.csv'
)

order_items = pd.read_csv(
    DATA_PATH + 'olist_order_items_dataset.csv'
)

# ==========================================
# 2. CONVERSÃO DAS DATAS
# ==========================================

date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors='coerce'
    )

# ==========================================
# 3. SELEÇÃO DOS PEDIDOS ENTREGUES
# ==========================================

orders_analysis = orders[
    orders['order_status'] == 'delivered'
].copy()

# ==========================================
# 4. VARIÁVEIS DERIVADAS
# ==========================================

orders_analysis['tempo_entrega_dias'] = (
    orders_analysis['order_delivered_customer_date']
    - orders_analysis['order_purchase_timestamp']
).dt.total_seconds() / (24 * 60 * 60)

orders_analysis['dias_atraso'] = (
    orders_analysis['order_delivered_customer_date']
    - orders_analysis['order_estimated_delivery_date']
).dt.total_seconds() / (24 * 60 * 60)

orders_analysis['situacao_entrega'] = np.where(
    orders_analysis['dias_atraso'] > 0,
    'Atrasado',
    'Dentro do prazo'
)

# ==========================================
# 5. GRÁFICO 1 — SITUAÇÃO DAS ENTREGAS
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=orders_analysis,
    x='situacao_entrega'
)

plt.title(
    'Quantidade de Pedidos por Situação da Entrega'
)

plt.xlabel('Situação da Entrega')
plt.ylabel('Quantidade de Pedidos')

plt.tight_layout()
plt.show()


# ==========================================
# 6. GRÁFICO 2 — TEMPO DE ENTREGA
# ==========================================

plt.figure(figsize=(10, 5))

sns.histplot(
    orders_analysis['tempo_entrega_dias'].dropna(),
    bins=40,
    kde=True
)

plt.title(
    'Distribuição do Tempo de Entrega'
)

plt.xlabel('Tempo de Entrega (dias)')
plt.ylabel('Quantidade de Pedidos')

plt.tight_layout()
plt.show()


# ==========================================
# 7. GRÁFICO 3 — DIAS DE ATRASO
# ==========================================

atrasados = orders_analysis[
    orders_analysis['dias_atraso'] > 0
]

plt.figure(figsize=(10, 5))

sns.histplot(
    atrasados['dias_atraso'].dropna(),
    bins=30,
    kde=True
)

plt.title(
    'Distribuição dos Dias de Atraso'
)

plt.xlabel('Dias de Atraso')
plt.ylabel('Quantidade de Pedidos')

plt.tight_layout()
plt.show()


# ==========================================
# 8. INTEGRAÇÃO COM CLIENTES
# ==========================================

orders_customers = orders_analysis.merge(
    customers[
        [
            'customer_id',
            'customer_state'
        ]
    ],
    on='customer_id',
    how='left'
)


# ==========================================
# 9. GRÁFICO 4 — TAXA DE ATRASO POR ESTADO
# ==========================================

taxa_estado = (
    orders_customers
    .groupby('customer_state')['situacao_entrega']
    .apply(
        lambda x:
        (x == 'Atrasado').mean() * 100
    )
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

taxa_estado.plot(
    kind='bar'
)

plt.title(
    'Taxa de Atraso por Estado'
)

plt.xlabel('Estado')
plt.ylabel('Taxa de Atraso (%)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==========================================
# 10. GRÁFICO 5 — TEMPO MÉDIO POR ESTADO
# ==========================================

tempo_estado = (
    orders_customers
    .groupby('customer_state')['tempo_entrega_dias']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))

tempo_estado.plot(
    kind='bar'
)

plt.title(
    'Tempo Médio de Entrega por Estado'
)

plt.xlabel('Estado')
plt.ylabel('Tempo Médio de Entrega (dias)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==========================================
# 11. GRÁFICO 6 — EVOLUÇÃO DA TAXA DE ATRASO
# ==========================================

orders_analysis['mes_compra'] = (
    orders_analysis[
        'order_purchase_timestamp'
    ]
    .dt.to_period('M')
    .astype(str)
)

atraso_mensal = (
    orders_analysis
    .groupby('mes_compra')['situacao_entrega']
    .apply(
        lambda x:
        (x == 'Atrasado').mean() * 100
    )
)

plt.figure(figsize=(12, 5))

atraso_mensal.plot()

plt.title(
    'Evolução Mensal da Taxa de Atraso'
)

plt.xlabel('Mês')
plt.ylabel('Taxa de Atraso (%)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==========================================
# 12. INTEGRAÇÃO COM ITENS DOS PEDIDOS
# ==========================================

orders_items = orders_analysis.merge(
    order_items[
        [
            'order_id',
            'price',
            'freight_value'
        ]
    ],
    on='order_id',
    how='left'
)


# ==========================================
# 13. GRÁFICO 7 — FRETE X TEMPO DE ENTREGA
# ==========================================

dados_frete = orders_items[
    [
        'freight_value',
        'tempo_entrega_dias'
    ]
].dropna()

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=dados_frete,
    x='freight_value',
    y='tempo_entrega_dias',
    alpha=0.4
)

plt.title(
    'Relação entre Valor do Frete e Tempo de Entrega'
)

plt.xlabel('Valor do Frete')
plt.ylabel('Tempo de Entrega (dias)')

plt.tight_layout()
plt.show()


# ==========================================
# 14. CORRELAÇÃO
# ==========================================

correlacao = dados_frete.corr()

print(
    '\nCorrelação entre frete e tempo de entrega:'
)

print(correlacao)


# ==========================================
# 15. RESUMO
# ==========================================

print(
    '''
Visualizações produzidas:

1. Situação das entregas;
2. Distribuição do tempo de entrega;
3. Distribuição dos dias de atraso;
4. Taxa de atraso por estado;
5. Tempo médio de entrega por estado;
6. Evolução mensal da taxa de atraso;
7. Relação entre valor do frete e tempo de entrega.

Os gráficos possuem finalidade exploratória e descritiva.
As associações observadas não devem ser interpretadas
automaticamente como relações de causalidade.
'''
)
