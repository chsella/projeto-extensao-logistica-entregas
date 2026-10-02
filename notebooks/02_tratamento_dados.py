import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# ==========================================
# 1. CARREGAMENTO DOS DADOS
# ==========================================

DATA_PATH = '../data/raw/'

orders = pd.read_csv(DATA_PATH + 'olist_orders_dataset.csv')
customers = pd.read_csv(DATA_PATH + 'olist_customers_dataset.csv')
order_items = pd.read_csv(DATA_PATH + 'olist_order_items_dataset.csv')
order_payments = pd.read_csv(DATA_PATH + 'olist_order_payments_dataset.csv')
order_reviews = pd.read_csv(DATA_PATH + 'olist_order_reviews_dataset.csv')
products = pd.read_csv(DATA_PATH + 'olist_products_dataset.csv')
sellers = pd.read_csv(DATA_PATH + 'olist_sellers_dataset.csv')

print('Bases carregadas com sucesso.')


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

print('Conversão das datas concluída.')


# ==========================================
# 3. VERIFICAÇÃO DE VALORES AUSENTES
# ==========================================

missing_orders = orders.isna().sum().sort_values(
    ascending=False
)

print('\nValores ausentes na base de pedidos:')
print(missing_orders)


# ==========================================
# 4. SELEÇÃO DOS PEDIDOS ENTREGUES
# ==========================================

orders_delivered = orders[
    orders['order_status'] == 'delivered'
].copy()

print('\nQuantidade de pedidos entregues:')
print(len(orders_delivered))


# ==========================================
# 5. CÁLCULO DO TEMPO DE ENTREGA
# ==========================================

orders_delivered['tempo_entrega_dias'] = (
    orders_delivered['order_delivered_customer_date']
    - orders_delivered['order_purchase_timestamp']
).dt.total_seconds() / (24 * 60 * 60)

print('\nResumo do tempo de entrega:')
print(
    orders_delivered['tempo_entrega_dias'].describe()
)


# ==========================================
# 6. CÁLCULO DOS DIAS DE ATRASO
# ==========================================

orders_delivered['dias_atraso'] = (
    orders_delivered['order_delivered_customer_date']
    - orders_delivered['order_estimated_delivery_date']
).dt.total_seconds() / (24 * 60 * 60)

print('\nResumo dos dias de atraso:')
print(
    orders_delivered['dias_atraso'].describe()
)


# ==========================================
# 7. CLASSIFICAÇÃO DO PRAZO
# ==========================================

orders_delivered['situacao_entrega'] = np.where(
    orders_delivered['dias_atraso'] > 0,
    'Atrasado',
    'Dentro do prazo'
)

print('\nQuantidade por situação da entrega:')
print(
    orders_delivered['situacao_entrega'].value_counts()
)


# ==========================================
# 8. TAXA DE ATRASO
# ==========================================

total_entregues = len(orders_delivered)

total_atrasados = (
    orders_delivered['situacao_entrega']
    .eq('Atrasado')
    .sum()
)

taxa_atraso = (
    total_atrasados / total_entregues * 100
)

print(
    f'\nTaxa de atraso: {taxa_atraso:.2f}%'
)


# ==========================================
# 9. VERIFICAÇÃO DE VALORES INVÁLIDOS
# ==========================================

tempo_negativo = (
    orders_delivered['tempo_entrega_dias'] < 0
).sum()

atraso_extremo = (
    orders_delivered['dias_atraso'] < -365
).sum()

print(
    '\nRegistros com tempo de entrega negativo:',
    tempo_negativo
)

print(
    'Registros com valores extremos de atraso:',
    atraso_extremo
)


# ==========================================
# 10. BASE FINAL PARA ANÁLISE
# ==========================================

orders_analysis = orders_delivered[
    [
        'order_id',
        'customer_id',
        'order_status',
        'order_purchase_timestamp',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
        'tempo_entrega_dias',
        'dias_atraso',
        'situacao_entrega'
    ]
].copy()

print('\nEstrutura da base final:')
print(orders_analysis.head())

print('\nDimensão da base final:')
print(orders_analysis.shape)
