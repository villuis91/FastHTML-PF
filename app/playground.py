from sklearn import datasets
from pandas import DataFrame


def list_loadable_datasets():
    return [ds for ds in dir(datasets) if ds.startswith("load")]


def load_dataset(dataset_load_attribute: str):
    attribute = getattr(datasets, dataset_load_attribute)
    return attribute()


def load_ds_preview(dataset_load_attribute: str):
    dataset = load_dataset(dataset_load_attribute)
    return DataFrame(dataset.data).head().to_html()


if __name__ == "__main__":
    print(load_dataset())
