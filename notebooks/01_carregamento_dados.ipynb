
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

DATA_PATH = '../data/raw/'

orders = pd.read_csv(DATA_PATH + 'olist_orders_dataset.csv')
customers = pd.read_csv(DATA_PATH + 'olist_customers_dataset.csv')
order_items = pd.read_csv(DATA_PATH + 'olist_order_items_dataset.csv')
order_payments = pd.read_csv(DATA_PATH + 'olist_order_payments_dataset.csv')
order_reviews = pd.read_csv(DATA_PATH + 'olist_order_reviews_dataset.csv')
products = pd.read_csv(DATA_PATH + 'olist_products_dataset.csv')
sellers = pd.read_csv(DATA_PATH + 'olist_sellers_dataset.csv')
geolocation = pd.read_csv(DATA_PATH + 'olist_geolocation_dataset.csv')
category_translation = pd.read_csv(
    DATA_PATH + 'product_category_name_translation.csv'
)

print('Arquivos carregados com sucesso.')

dimensoes = pd.DataFrame({
    'base': [
        'orders',
        'customers',
        'order_items',
        'order_payments',
        'order_reviews',
        'products',
        'sellers',
        'geolocation',
        'category_translation'
    ],
    'linhas': [
        orders.shape[0],
        customers.shape[0],
        order_items.shape[0],
        order_payments.shape[0],
        order_reviews.shape[0],
        products.shape[0],
        sellers.shape[0],
        geolocation.shape[0],
        category_translation.shape[0]
    ],
    'colunas': [
        orders.shape[1],
        customers.shape[1],
        order_items.shape[1],
        order_payments.shape[1],
        order_reviews.shape[1],
        products.shape[1],
        sellers.shape[1],
        geolocation.shape[1],
        category_translation.shape[1]
    ]
})

print('\nDimensões das bases:')
print(dimensoes)

print('\nPrimeiros registros da base de pedidos:')
print(orders.head())

print('\nTipos das variáveis:')
print(orders.dtypes)

print('\nValores ausentes:')
print(orders.isna().sum().sort_values(ascending=False))

duplicados = pd.DataFrame({
    'base': [
        'orders',
        'customers',
        'order_items',
        'order_payments',
        'order_reviews',
        'products',
        'sellers'
    ],
    'duplicados': [
        orders.duplicated().sum(),
        customers.duplicated().sum(),
        order_items.duplicated().sum(),
        order_payments.duplicated().sum(),
        order_reviews.duplicated().sum(),
        products.duplicated().sum(),
        sellers.duplicated().sum()
    ]
})

print('\nRegistros duplicados:')
print(duplicados)
