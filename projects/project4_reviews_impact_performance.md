# 课题 4：评论与口碑对房源表现的影响

> 提示：本课题以相关性分析 + 简单预测模型为主，适合作为“基础难度”选题。  
> 通用规范（EDA、Train/Val/Test、Git、报告撰写等）请参考课程总 README。

---

## 一、课题背景与核心问题

Airbnb 房源的评论数量和评分结构，通常会被认为影响其收入和入住率：  
- 高评分是否一定带来更多订单和更高 RevPAR？  
- 哪一维评分更“值钱”——清洁、位置、还是性价比？  
- 评论数量和评分高低之间如何共同作用？

本课题希望量化“口碑与表现”的关系，并构建简单模型预测“高收益房源”。

---

## 二、数据字段建议

### 1. Listings（房源级口碑与表现）

- 口碑相关：  
  `num_reviews, rating_overall, rating_cleanliness, rating_location, rating_value, rating_accuracy, rating_communication, rating_checkin`
- 表现指标：  
  `ttm_revenue, ttm_occupancy, ttm_revpar, l90d_revenue, l90d_occupancy`

### 2. Reviews Data（可选：时间维度评论动态）

- 示例字段：`listing_id, date, num_reviews, reviewers`（可按月聚合）

> 若时间序列分析难度较大，可只做房源级横截面分析。

---

## 三、必做任务

### 1. 房源级相关性分析

以某个城市为例，在 listing 这一层面，完成：

1. 计算 `rating_overall` 与 `ttm_revpar / ttm_occupancy` 的相关系数（如 Pearson）；
2. 分别计算各维度评分（`rating_cleanliness, rating_location, rating_value, ...`）与表现指标之间的相关性；
3. 绘制相关性热力图或条形图，对不同评分维度的影响做排序。

> 要求在报告中明确说明：**相关性 ≠ 因果关系**，本课题结论主要是“相关分析”。

### 2. 评论数量与口碑的联合影响

构造若干类别，例如：

- 高评分（如 `rating_overall > 4.8`）且评论数较多（`num_reviews` 高分位）；  
- 高评分但评论数较少；  
- 评分一般但评论数较多；  
- 评分较低且评论数较少等。

对于各类别，比较其：

- `ttm_revpar` 的分布；  
- `ttm_occupancy` 的分布。

建议使用箱线图 / 小提琴图 等方式展示，观察是否存在明显差异。

### 3. 简单回归 / 分类模型

目标：利用评分和评论数量信息，预测一个房源是否为“高收益房源”。

1. 定义“高收益房源”的标签（建议与课题 1 对齐，如 top 25% RevPAR）；  
2. 选择合适特征集：
   - 各维度评分 + `num_reviews`；
3. 至少构建两个模型：
   - 基线：Logistic Regression；  
   - 树模型：如 Random Forest / XGBoost 等。
4. 对比模型在 Accuracy / F1 / AUC 等指标上的表现，并分析：
   - 哪些特征在模型中权重更大？  
   - 是否与相关性分析阶段的结论一致？

---

## 四、选做任务（加分项）

1. **评论时间序列与“评论爆发期”**  
   - 使用 Reviews Data，按月份统计每个 listing 的 `num_reviews`；  
   - 定义“评论爆发期”（某些月份评论数显著高于平时）；  
   - 观察爆发期后若干个月的 `occupancy / revenue` 是否有明显提升。

2. **“差评冲击”的敏感度分析（近似）**  
   - 基于线性回归模型，估计 `rating_overall` 每下降 0.1–0.3 分时，`ttm_revpar` 的平均变化幅度；  
   - 讨论：如果一条差评把评分从 4.9 拉到 4.6，对 RevPAR 的可能影响有多大？  
   > 请在报告中强调：这是基于相关性模型的“近似估计”，不代表严格因果结论。
