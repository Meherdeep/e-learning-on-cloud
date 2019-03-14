import pandas as pd

from credentials import mongodb_parameters
from pymongo import MongoClient

data = pd.read_csv('products.csv')
print('Shape: ', data.shape)

def data_to_mongo(params):

    product_list = []

    client = MongoClient(params['dblink'])
    db = client[params['database_name']]

    for idx in range(data.shape[0]):
        each = data.iloc[idx]
        product_info = {
            'image': each['Image'],
            'category': each['Category'],
            'item': each['Item'],
            'price': each['Price']
        }
        product_list.append(product_info)
    
    print(product_list[0])
    print('Lenght: ', len(product_list))
    db.products.insert_many(product_list)
    print('Data written to mongoDB')

if __name__ == "__main__":

    params = mongodb_parameters()
    data_to_mongo(params)