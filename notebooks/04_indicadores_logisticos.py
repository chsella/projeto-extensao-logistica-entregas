import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

sellers = pd.read_csv(
    DATA_PATH + 'olist_sellers_dataset.csv'
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
# 4. INDICADORES DE TEMPO
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
# 5. KPI — TOTAL DE PEDIDOS ENTREGUES
# ==========================================

total_pedidos = len(orders_analysis)

# ==========================================
# 6. KPI — PEDIDOS DENTRO DO PRAZO
# ==========================================

pedidos_no_prazo = (
    orders_analysis['situacao_entrega']
    == 'Dentro do prazo'
).sum()

# ==========================================
# 7. KPI — PEDIDOS ATRASADOS
# ==========================================

pedidos_atrasados = (
    orders_analysis['situacao_entrega']
    == 'Atrasado'
).sum()

# ==========================================
# 8. KPI — TAXA DE ATRASO
# ==========================================

taxa_atraso = (
    pedidos_atrasados
    / total_pedidos
) * 100

# ==========================================
# 9. KPI — TAXA DE ENTREGA NO PRAZO
# ==========================================

taxa_no_prazo = (
    pedidos_no_prazo
    / total_pedidos
) * 100

# ==========================================
# 10. KPI — TEMPO MÉDIO DE ENTREGA
# ==========================================

tempo_medio_entrega = (
    orders_analysis['tempo_entrega_dias']
    .mean()
)

# ==========================================
# 11. KPI — MEDIANA DO TEMPO DE ENTREGA
# ==========================================

mediana_entrega = (
    orders_analysis['tempo_entrega_dias']
    .median()
)

# ==========================================
# 12. KPI — ATRASO MÉDIO
# ==========================================

atraso_medio = (
    orders_analysis.loc[
        orders_analysis['dias_atraso'] > 0,
        'dias_atraso'
    ].mean()
)

# ==========================================
# 13. TABELA DE INDICADORES
# ==========================================

indicadores = pd.DataFrame({
    'Indicador': [
        'Total de pedidos entregues',
        'Pedidos dentro do prazo',
        'Pedidos atrasados',
        'Taxa de entrega no prazo (%)',
        'Taxa de atraso (%)',
        'Tempo médio de entrega (dias)',
        'Mediana do tempo de entrega (dias)',
        'Atraso médio dos pedidos atrasados (dias)'
    ],
    'Valor': [
        total_pedidos,
        pedidos_no_prazo,
        pedidos_atrasados,
        taxa_no_prazo,
        taxa_atraso,
        tempo_medio_entrega,
        mediana_entrega,
        atraso_medio
    ]
})

print('\n==========================================')
print('INDICADORES LOGÍSTICOS')
print('==========================================')

print(indicadores)

# ==========================================
# 14. INDICADORES POR ESTADO
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

indicadores_estado = (
    orders_customers
    .groupby('customer_state')
    .agg(
        pedidos=('order_id', 'count'),
        tempo_medio_entrega=('tempo_entrega_dias', 'mean'),
        atraso_medio=('dias_atraso', 'mean')
    )
)

indicadores_estado['taxa_atraso'] = (
    orders_customers
    .groupby('customer_state')['situacao_entrega']
    .apply(
        lambda x:
        (x == 'Atrasado').mean() * 100
    )
)

indicadores_estado = (
    indicadores_estado
    .sort_values(
        'taxa_atraso',
        ascending=False
    )
)

print('\n==========================================')
print('INDICADORES POR ESTADO')
print('==========================================')

print(indicadores_estado)

# ==========================================
# 15. INDICADORES POR VENDEDOR
# ==========================================

orders_sellers = orders_analysis.merge(
    order_items[
        [
            'order_id',
            'seller_id',
            'price',
            'freight_value'
        ]
    ],
    on='order_id',
    how='left'
)

indicadores_vendedor = (
    orders_sellers
    .groupby('seller_id')
    .agg(
        pedidos=('order_id', 'nunique'),
        tempo_medio_entrega=('tempo_entrega_dias', 'mean'),
        frete_medio=('freight_value', 'mean'),
        valor_medio_produto=('price', 'mean')
    )
)

indicadores_vendedor['taxa_atraso'] = (
    orders_sellers
    .groupby('seller_id')['situacao_entrega']
    .apply(
        lambda x:
        (x == 'Atrasado').mean() * 100
    )
)

print('\n==========================================')
print('INDICADORES POR VENDEDOR')
print('==========================================')

print(
    indicadores_vendedor.head(20)
)

# ==========================================
# 16. RELAÇÃO ENTRE FRETE E ENTREGA
# ==========================================

frete_entrega = orders_sellers[
    [
        'order_id',
        'freight_value',
        'tempo_entrega_dias',
        'dias_atraso'
    ]
].dropna()

correlacao_frete_tempo = (
    frete_entrega[
        [
            'freight_value',
            'tempo_entrega_dias'
        ]
    ].corr()
)

print('\n==========================================')
print('CORRELAÇÃO ENTRE FRETE E TEMPO DE ENTREGA')
print('==========================================')

print(correlacao_frete_tempo)

# ==========================================
# 17. GRÁFICO — TAXA DE ATRASO POR ESTADO
# ==========================================

plt.figure(figsize=(12, 6))

indicadores_estado[
    'taxa_atraso'
].plot(kind='bar')

plt.title('Taxa de Atraso por Estado')
plt.xlabel('Estado')
plt.ylabel('Taxa de Atraso (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ==========================================
# 18. CONCLUSÃO
# ==========================================

print(
    '''
Indicadores logísticos calculados:

- Total de pedidos entregues;
- Pedidos dentro do prazo;
- Pedidos atrasados;
- Taxa de atraso;
- Taxa de entrega no prazo;
- Tempo médio de entrega;
- Mediana do tempo de entrega;
- Atraso médio;
- Indicadores por estado;
- Indicadores por vendedor;
- Relação entre frete e tempo de entrega.

Os indicadores possuem finalidade descritiva e exploratória.
Uma associação observada entre variáveis não significa,
por si só, uma relação de causalidade.
'''
)
