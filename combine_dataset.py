import pandas as pd
import os

def combine_all_csv(folder="dataset"):
    all_data = []
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, filename))
            all_data.append(df)
    data = pd.concat(all_data, ignore_index=True)
    return data

if __name__ == "__main__":
    data = combine_all_csv()
    print(data.head())
    print(f"Jumlah data total: {len(data)}")
    data.to_csv("dataset_all.csv", index=False)
    print("[INFO] Dataset gabungan disimpan sebagai dataset_all.csv")
