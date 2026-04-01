---
comments: true
---

# Topological Depth vs. Pipeline Breadth (369/4143)

!!! note

    This is a writeup for the [Predict Customer Churn](https://www.kaggle.com/competitions/predict-customer-churn) competition. This post is a copy from my Kaggle [post](https://www.kaggle.com/competitions/playground-series-s6e3/writeups/topological-depth-vs-pipeline-breadth-3694143).

Congratulations to all Kagglers who received their anticipated scores!

While a rank of 369/4143 did not meet my expectations, as I have been struggling around top 10%, I would like to share a comparison of two philosophies: building a complex model stack with simple feature engineering and building a simple model stack with complex feature engineering.

## Overview: The Performance Gap

`v3` is the my pipeline with a 3-level model stack and minimal feature engineering. `v5` and `v6` have 2-level stack with more complicated features. Despite the added complexity, my Private LB score regressed from **0.91591** in `v3` to **0.91453** in `v5`. 

| Version     | Strategic Focus                                 | CV Score    | Private LB  | LB Gap      |
| :---------- | :---------------------------------------------- | :---------- | :---------- | :---------- |
| **code_v3** | **10-Folds, Hard Pseudo-labels, 7-Model Depth** | **0.91843** | **0.91591** | **0.00252** |
| code_v5     | 5-Folds, Soft Labels, External Target Encoding  | 0.91714     | 0.91453     | 0.00261     |
| code_v6     | 5-Folds, Magic Interactions, Feature Isolation  | 0.91811     | 0.91497     | 0.00314     |

## Philosophy A: Topological Depth (v3)

The success of `v3` came from its **structural reliability**. Instead of relying on raw feature power, I focused on high-fold cross-validation and a hierarchical ensemble that forced model diversity through different data splits.

In `v3`, I splited the dataset down to two subsets: A with basic, raw features and B with One Hot Encoding and Standard Scaling.

Notice that Ridge and Torch MLP need to be trained on scaled features, while GBDT can be trained on raw features. This is because Ridge and Torch MLP are linear models, while GBDT is a tree-based model.

I used `DART` mode in LGBM, as it is more robust to overfitting than `GBDT`. Do notice that `DART` takes much more time to train.

In Level 2, I input ridge as feature to XGBoost to increase the diversity of features. Finally, I use `hillclimbing` to optimize the weights of the ensemble.

![v3 Architecture](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21970084%2Fe72a53efcef7caa64925acc91db269df%2Fv3-architecture.png?generation=1775013633159307&alt=media)

### Diversity
By using a 3-level stack, the diversity of models is increased. The L2 stacker filtered out local noisy predictions before the final weight optimization, which buffered against Private LB shifts.

## Philosophy B: Pipeline Breadth (v5/v6)

In `v5`, I pivoted toward pipeline breadth, introducing External Target Encoding and Soft Pseudo-labeling. However, because the size of the dataset is significantly increased, I compressed the topology into a 2-level structure and reduced the folds from 10 to 5 to save time and space, as I encountered memory limit exceeded error for several times.

![v5 Architecture](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21970084%2F87a617eae10a1301678941e32d8e60c2%2Fv5-architecture.png?generation=1775019973546713&alt=media)

## Diversity Comparison

### Correlation Evolution

One of the direct cause of the performance drop is the loss of diversity. In `v3`, the models were quite independent. In `v5`, the advanced features caused the models to correlate their errors, making the ensemble increasingly fragile.

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21970084%2F1d269fad9e2cd79d3b096b636451b99a%2Fv3_correlation.png?generation=1775020056897986&alt=media)

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21970084%2F319881694eb6a86a0539b220ef5dd4f7%2Fv5_correlation.png?generation=1775020067340682&alt=media)

![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F21970084%2F9a531c39cbba61733528a25074ed6d9b%2Fv6_correlation.png?generation=1775020086694143&alt=media)

## Final Insights

1.  **Hard Labels vs Soft Labels**: Hard pseudo-labels (0/1) with a high confidence threshold (95%+) proved to be more effective than iterative soft-labeling in this competition. This may be because soft-labeling often amplified early-stage training bias.
2.  **The Shortcut Paradox**: My `v6` approach of **Feature Isolation**—forcing GBDTs to train on raw categories without the "easy" math derivatives (Ratio, Diff)—forced the models to learn more robust internal representations and reclaimed significant LB ground.

Therefore, it is important to build a solid, comprehensive model stack, as it could be of more help initially than a complex pipeline.

Thanks for reading! Keep on keeping on at next Playground!
