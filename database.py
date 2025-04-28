from pymongo import MongoClient


def write_df_to_mongoDB( my_df, database_name = 'flights' , collection_name = 'tickets', mongodb_port = 27017):

    client = MongoClient('localhost',int(mongodb_port))
    db = client[database_name]
    collection = db[collection_name]
    df_cleaned = my_df.drop(columns=['Unnamed: 0'])  
    data_to_insert = df_cleaned.to_dict(orient='records')

    client = MongoClient(f'mongodb://localhost:{mongodb_port}/')  
    db = client[database_name]  
    collection = db[collection_name]  


    insert_result = collection.insert_many(data_to_insert)
    print(f"Number of document inserted: {len(insert_result.inserted_ids)}")
    print('Done')
    return