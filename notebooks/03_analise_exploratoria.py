import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

# ==========================================
# 1. CARREGAMENTO E PREPARAÇÃO
# ==========================================

DATA_PATH = '../data/raw/'

orders = pd.read_csv(DATA_PATH + 'olist_orders_dataset.csv')
customers = pd.read_csv(DATA_PATH + 'olist_customers_dataset.csv')
order_items = pd.read_csv(DATA_PATH + 'olist_order_items_dataset.csv')
sellers = pd.read_csv(DATA_PATH + 'olist_sellers_dataset.csv')

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

# Consideramos pedidos efetivamente entregues
orders_analysis = orders[
    orders['order_status'] == 'delivered'
].copy()

# Tempo de entrega
orders_analysis['tempo_entrega_dias'] = (
    orders_analysis['order_delivered_customer_date']
    - orders_analysis['order_purchase_timestamp']
).dt.total_seconds() / (24 * 60 * 60)

# Dias de atraso
orders_analysis['dias_atraso'] = (
    orders_analysis['order_delivered_customer_date']
    - orders_analysis['order_estimated_delivery_date']
).dt.total_seconds() / (24 * 60 * 60)

# Classificação
orders_analysis['situacao_entrega'] = np.where(
    orders_analysis['dias_atraso'] > 0,
    'Atrasado',
    'Dentro do prazo'
)

print('Base preparada para análise exploratória.')


# ==========================================
# 2. ESTATÍSTICAS DESCRITIVAS
# ==========================================

print('\nEstatísticas do tempo de entrega:')
print(
    orders_analysis['tempo_entrega_dias'].describe()
)

print('\nEstatísticas dos dias de atraso:')
print(
    orders_analysis['dias_atraso'].describe()
)


# ==========================================
# 3. SITUAÇÃO DAS ENTREGAS
# ==========================================

situacao = (
    orders_analysis['situacao_entrega']
    .value_counts()
)

print('\nSituação das entregas:')
print(situacao)


# ==========================================
# 4. PERCENTUAL DE ENTREGAS
# ==========================================

percentual_situacao = (
    orders_analysis['situacao_entrega']
    .value_counts(normalize=True) * 100
)

print('\nPercentual por situação:')
print(percentual_situacao)


# ==========================================
# 5. GRÁFICO — ENTREGAS NO PRAZO X ATRASADAS
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=orders_analysis,
    x='situacao_entrega'
)

plt.title('Situação das Entregas')
plt.xlabel('Situação')
plt.ylabel('Quantidade de Pedidos')
plt.tight_layout()

plt.show()


# ==========================================
# 6. DISTRIBUIÇÃO DO TEMPO DE ENTREGA
# ==========================================

plt.figure(figsize=(10, 5))

sns.histplot(
    orders_analysis['tempo_entrega_dias'].dropna(),
    bins=40,
    kde=True
)

plt.title('Distribuição do Tempo de Entrega')
plt.xlabel('Tempo de Entrega (dias)')
plt.ylabel('Quantidade de Pedidos')
plt.tight_layout()

plt.show()


# ==========================================
# 7. DISTRIBUIÇÃO DOS DIAS DE ATRASO
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

plt.title('Distribuição dos Dias de Atraso')
plt.xlabel('Dias de Atraso')
plt.ylabel('Quantidade de Pedidos')
plt.tight_layout()

plt.show()


# ==========================================
# 8. ESTADOS DOS CLIENTES
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

taxa_estado = (
    orders_customers
    .groupby('customer_state')['situacao_entrega']
    .apply(
        lambda x: (x == 'Atrasado').mean() * 100
    )
    .sort_values(ascending=False)
)

print('\nTaxa de atraso por estado:')
print(taxa_estado)


# ==========================================
# 9. GRÁFICO — TAXA DE ATRASO POR ESTADO
# ==========================================

plt.figure(figsize=(12, 6))

taxa_estado.plot(
    kind='bar'
)

plt.title('Taxa de Atraso por Estado')
plt.xlabel('Estado')
plt.ylabel('Taxa de Atraso (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ==========================================
# 10. EVOLUÇÃO TEMPORAL
# ==========================================

orders_analysis['mes_compra'] = (
    orders_analysis['order_purchase_timestamp']
    .dt.to_period('M')
    .astype(str)
)

atraso_mensal = (
    orders_analysis
    .groupby('mes_compra')['situacao_entrega']
    .apply(
        lambda x: (x == 'Atrasado').mean() * 100
    )
)

print('\nTaxa de atraso por mês:')
print(atraso_mensal)


# ==========================================
# 11. GRÁFICO — EVOLUÇÃO DA TAXA DE ATRASO
# ==========================================

plt.figure(figsize=(12, 5))

atraso_mensal.plot()

plt.title('Evolução Mensal da Taxa de Atraso')
plt.xlabel('Mês')
plt.ylabel('Taxa de Atraso (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ==========================================
# 12. CONCLUSÃO DA ANÁLISE EXPLORATÓRIA
# ==========================================

print('\nAnálise exploratória concluída.')

print(
    '''
Principais dimensões analisadas:

- Tempo de entrega;
- Dias de atraso;
- Entregas dentro e fora do prazo;
- Distribuição dos atrasos;
- Diferenças entre estados;
- Evolução temporal da taxa de atraso.

Os resultados devem ser interpretados como associações
observadas nos dados e não como relações de causalidade.
'''
)
