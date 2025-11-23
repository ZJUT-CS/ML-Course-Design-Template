# 课题 1：房源收益预测与“优质房源画像”

> 提示：本课题说明只包含本题特定要求。  
> 通用规范（EDA、Train/Val/Test、Git、报告撰写等）请参考课程总 README。

---

## 一、课题背景与核心问题

在某个城市市场里，哪些房源是“高收益房源”？  
能否根据房源属性预测 RevPAR / 收益水平，并总结“优质房源画像”，为运营方提供选房与改造建议？

---

## 二、数据字段建议

数据表：**Listings Data（房源静态 + TTM / L90 天表现）**

示例字段（可酌情增删）：

- **位置与规模**  
  `country, state, city, latitude, longitude, guests, bedrooms, beds, baths`

- **类型与运营方式**  
  `listing_type, room_type, instant_book, professional_management, superhost`

- **价格与费用**  
  `currency, cleaning_fee, extra_guest_fee, min_nights, cancellation_policy`

- **口碑**  
  `num_reviews, rating_overall, rating_cleanliness, rating_location, rating_value, ...`

- **收益 & 表现（重点）**  
  - 过去 12 个月：`ttm_revenue, ttm_avg_rate, ttm_occupancy, ttm_revpar, ...`
  - 最近 90 天：`l90d_revenue, l90d_avg_rate, l90d_occupancy, l90d_revpar, ...`

> 注意：预测 `ttm_revpar` 时，**不要**把 `ttm_revpar` 本身或等价变形（如 `ttm_revenue / ttm_total_days`）放入特征，以免标签泄露。

---

## 三、必做任务

### 1. 数据构建与清洗

1. 选定一个城市（`city`）或“国家 + 城市”组合，过滤出该市场全部房源；
2. 删除明显异常记录，例如：  
   - `ttm_total_days` 不合理；  
   - `ttm_occupancy` 超出 `[0, 1]` 范围；
3. 处理关键字段缺失值（如 `ttm_revpar, guests, room_type` 等），并说明处理策略（删除 / 填补的依据）。

### 2. 任务设定：收益预测

从以下两种设定中任选 **一种**（也可以两个都做，但至少完成一个）：

1. **回归任务**  
   - 目标：预测 `ttm_revpar`（或 `l90d_revpar`）的数值。
2. **分类任务**  
   - 按 `ttm_revpar` 或 `ttm_revenue` 做分位数分组，例如：  
     - 二分类示例：top 30% = 高收益，bottom 30% = 低收益（中间样本可丢弃）；  
     - 三分类示例：top 25% / middle 50% / bottom 25%。  

需在报告中说明你的标签划分方式和理由。

### 3. 特征工程

至少构造/使用以下类型特征，并说明计算方式：

- **房源规模**：  
  - 例如客容量、卧室数、浴室数及其组合（如每卧室可住人数等）；
- **运营属性**：  
  - `superhost, instant_book, professional_management` 等布尔特征；
- **价格结构**：  
  - `cleaning_fee / ttm_avg_rate` 比值；  
  - 是否存在 `extra_guest_fee`；
- **位置特征（可选）**：  
  - 简单经纬度分箱；  
  - 或粗粒度区域划分（如城区 / 郊区）。

要求在文档中说明：

- 哪些是原始字段，哪些是衍生特征；
- 如何避免把“目标本身”或明显反映目标的特征加入模型。

### 4. 模型训练与对比

至少实现并对比 **两个模型**：

1. **基线模型**（简单可解释）  
   - 回归：`Linear Regression`  
   - 分类：`Logistic Regression`
2. **树模型**（非线性 & 更强拟合能力）  
   - 如 `Random Forest` 或 `XGBoost / LightGBM`

评估指标示例：

- 回归：MAE、RMSE、R²（至少 2 个）；
- 分类：Accuracy、F1、AUC（至少 2 个）。

建议绘制（按任务类型二选一）：

- 回归：预测值 vs 真实值散点图、残差分布图；
- 分类：混淆矩阵 + ROC 或 PR 曲线。

### 5. 优质房源画像与解释

使用特征重要性或 SHAP 等方法，分析：

- 哪些特征对预测结果影响最大；
- 哪些特征与“高收益”最相关。

在此基础上，总结 **3–5 条“优质房源画像”**，用业务语言描述，例如：

- “2–3 间卧室的整套房 + 超级房东 + 提供厨房设施的房源，其 TTM RevPAR 显著更高。”
- “专业管理（professional_management）的房源在同价位段的 RevPAR 高于普通房东。”

要求这一部分尽量写给“运营经理”看，少用或解释专业术语。

---

## 四、选做任务（加分项）

- 比较 **TTM 指标** vs **L90D 指标** 作为标签时：  
  - 模型表现是否有明显差异？  
  - 特征重要性排序是否发生变化？  
  （可以理解为“长期 vs 短期收益”的差异分析）

- 按 `room_type` 或 `listing_type` 分层建模：  
  - 例如「整套房」 vs 「合住房」；  
  - 观察不同子市场中的规律是否一致。

- 使用地理可视化：  
  - 基于 `latitude, longitude` 在地图上标记“高收益房源”和“低收益房源”；  
  - 观察其空间分布特点（是否集中在景区 / 核心商圈等）。