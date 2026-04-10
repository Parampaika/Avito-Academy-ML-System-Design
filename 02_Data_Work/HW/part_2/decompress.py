import pandas as pd

def decompress_data(input_parquet, output_csv):
    df = pd.read_parquet(input_parquet)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    decompress_data('compressed_data.parquet', 'restored_data.csv')