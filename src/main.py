import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from utils import load_iris_dataset


def parse_args():
    parser = argparse.ArgumentParser(
        description="ML Course Design Baseline Example (Iris Dataset)"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="logistic",
        help="Model type (currently only 'logistic' is implemented)",
    )
    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Test set ratio (0-1)",
    )
    return parser.parse_args()


def train_and_eval(args):
    """示例训练与评估流程。

    提示：
        - 实际项目中，你需要根据自己的数据与任务，改写本函数：
          * 换成自己的数据加载函数；
          * 使用适合任务的模型与评价指标；
          * 增加超参数、模型保存、绘图等功能。
        - 可以保留本函数作为最简单的 baseline 用例。
    """
    # 示例：使用 iris 数据集
    X_train, X_test, y_train, y_test = load_iris_dataset(test_size=args.test_size)

    if args.model == "logistic":
        model = LogisticRegression(max_iter=200)
    else:
        raise ValueError(f"Unknown model type: {args.model}")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"[Baseline] Model: {args.model}, Test Accuracy: {acc:.4f}")


def main():
    args = parse_args()
    train_and_eval(args)


if __name__ == "__main__":
    main()
