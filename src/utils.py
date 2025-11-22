import pandas as pd
from sklearn.model_selection import train_test_split


def load_iris_dataset(test_size: float = 0.2, random_state: int = 42):
    """
    示例数据加载函数：使用 sklearn 自带 iris 数据集。

    说明：
        - 本函数仅用于验证环境与示例代码；
        - 完成课程项目时，建议在本文件中新增 / 修改函数，
          例如 `load_tabular_dataset`, `load_text_dataset` 等，
          用于加载你们自己的数据。

    返回：
        X_train, X_test, y_train, y_test
    """
    from sklearn.datasets import load_iris

    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target

    return train_test_split(X, y, test_size=test_size, random_state=random_state)
