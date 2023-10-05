import pandas as pd

bin_data = pd.read_csv("dataset/ccbin.csv")

def checkbin(bin):
    bin_split = bin[0:6]
    bin_query = int(bin_split)
    bin_dataset = bin_data["iin_start"]
    bin_search=bin_data[(bin_dataset) == bin_query]
    try:
        binfetch_res = bin_search.to_dict(orient='records')[0]
        fetched_bins = {key: str(value).replace('.0','').replace('nan',"None") for key, value in binfetch_res.items()}

        return fetched_bins
    except Exception as e:
        return f"{bin} is not in dataset"