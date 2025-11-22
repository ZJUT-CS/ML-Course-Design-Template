# notebooks 目录说明

建议在此目录下创建 Jupyter Notebook 文件，用于：

- 数据探索（EDA）；
- 特征工程尝试；
- 模型原型实验与可视化。

注意事项：

1. Notebook 更适合做“试验台”，最终可复现的训练与评估流程请整理到 `src/main.py` 等脚本中；
2. 若 Notebook 较多，建议在文件名中注明日期或用途，例如：
   - `01_eda_basic.ipynb`
   - `02_baseline_model.ipynb`
   - `03_model_xgboost.ipynb`
3. 不要把无关的临时输出（如大体积中间结果文件）提交到仓库中。
