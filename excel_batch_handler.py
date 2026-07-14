import os
import pandas as pd

def batch_read_product_excel(folder_path):
    """
    批量读取外贸、抖店产品Excel文件，整合商品信息
    """
    total_data = []
    for file in os.listdir(folder_path):
        if file.endswith((".xlsx",".xls")):
            df = pd.read_excel(os.path.join(folder_path, file))
            total_data.append(df)
    combine_df = pd.concat(total_data)
    print(f"Total product rows: {len(combine_df)}")
    return combine_df

if __name__ == "__main__":
    # Example for hydraulic‑parts and 1688 goods data
    data = batch_read_product_excel("./product_files")
