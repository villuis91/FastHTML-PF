from sklearn import datasets
from pandas import DataFrame

def list_loadable_datasets():
    return [ds for ds in dir(datasets) if ds.startswith("load")]

def load_dataset(dataset_load_attribute="load_iris"):
    attribute = getattr(datasets, dataset_load_attribute)
    return attribute()

def load_ds_preview(dataset=load_dataset()):
    return DataFrame(dataset.data).to_html()



if __name__ == "__main__":
    print(load_dataset())
