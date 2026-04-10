import pandas as pd

def compress_data(input_csv, output_parquet):
    df = pd.read_csv(input_csv)
    
    df['user_id'] = df['user_id'].astype('category')
    df['item_id'] = df['item_id'].astype('category')
    
    df['category_id'] = df['category_id'].astype('int16')
    df['microcategory_id'] = df['microcategory_id'].astype('int16')
    df['location_id'] = df['location_id'].astype('int16')
    df['timestamp'] = df['timestamp'].astype('int32')
    df['class'] = df['class'].astype('int8')
    
    df['model_a_score'] = df['model_a_score'].astype('float32')
    df['model_b_score'] = df['model_b_score'].astype('float32')
    df['price'] = df['price'].astype('float32')
    
    df = df.sort_values(by=['category_id', 'microcategory_id', 'location_id', 'user_id'])
    
    df.to_parquet(output_parquet, engine='pyarrow', compression='brotli', index=False)
    
if __name__ == "__main__":
    compress_data('normal_data.csv', 'compressed_data.parquet')