# Project 2: Data Classification Using AI — Iris Species Classifier

A supervised learning classification model built as part of the DecodeLabs AI Engineering Internship (Batch 2026). This project uses the classic Iris dataset to train, test, and validate a K-Nearest Neighbors (KNN) model that predicts flower species from measurements.

## Overview

Unlike the rule-based logic of Project 1, this project moves into **supervised learning** — the model isn't given explicit rules, but instead learns patterns from labeled historical data and generalizes that to classify new, unseen samples.

## Dataset

The **Iris dataset** — a standard benchmark dataset in machine learning:
- **150 samples**, evenly split across 3 species (balanced dataset)
- **3 classes**: Setosa, Versicolor, Virginica
- **4 features** per sample: sepal length, sepal width, petal length, petal width (all in cm)

## Pipeline

1. **Load & explore the dataset** — inspect structure, feature ranges, and class balance
2. **Feature scaling** — applied `StandardScaler` to normalize all features to mean = 0, variance = 1, preventing any single feature from dominating due to scale differences
3. **Train-test split** — data shuffled and split (80/20) to ensure the model is evaluated on unseen data
4. **Model training** — K-Nearest Neighbors (KNN) classifier:
   ```python
   model = KNeighborsClassifier(n_neighbors=5)
   model.fit(X_train, y_train)
   predictions = model.predict(X_test)
   ```
5. **Evaluation** — assessed using a confusion matrix (True Positives, False Positives, False Negatives, True Negatives) and metrics beyond raw accuracy, since accuracy alone can be misleading on certain datasets

## Key Concepts Applied

- **Feature scaling** — raw, unscaled data can bias distance-based algorithms like KNN toward features with larger numeric ranges
- **K-Nearest Neighbors** — classifies a new sample based on the majority class among its "k" closest neighbors in feature space
- **Choosing K** — a small K (e.g. K=1) risks overfitting to noise; a large K risks underfitting/over-generalizing. The optimal K is typically found at the "elbow" of an error-rate vs. K plot.
- **Confusion Matrix & F1 Score** — used instead of relying solely on accuracy, since accuracy can be misleadingly high even when a model performs poorly on minority classes

## Tech Stack

- Python 3
- Jupyter Notebook
- [scikit-learn](https://scikit-learn.org/) — dataset, preprocessing, KNN model, evaluation metrics
- [pandas](https://pandas.pydata.org/) / [numpy](https://numpy.org/) — data handling

## How to Run

1. Open `Data Classificatiion Task 2.ipynb` in Jupyter Notebook, JupyterLab, or VS Code (with the Jupyter extension).
2. Ensure required packages are installed:
   ```bash
   pip install scikit-learn pandas numpy
   ```
3. Run all cells from top to bottom.

## Project Structure

```
project-2-classification/
  Data Classificatiion Task 2.ipynb   # full notebook: load, scale, split, train, evaluate
  README.md                            # this file
```

## Notes

- This project intentionally uses a well-known, clean benchmark dataset (Iris) to focus on mastering the core supervised learning pipeline — load, scale, split, train, predict, evaluate — before working with messier, real-world data.
- The same IPO (Input → Process → Output) structure used in Projects 1 and 3 applies here: Input (scaled features) → Process (KNN training/prediction) → Output (evaluated predictions).
