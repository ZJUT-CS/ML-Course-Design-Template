import pandas as pd
from sklearn.model_selection import train_test_split


def load_iris_dataset(test_size=0.2, random_state=42):
    """
    示例数据加载函数：使用 sklearn 自带 iris 数据集。
    真实项目中建议改成加载你自己的数据。
    """
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
