import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

DATA_PATH = "data/data.csv"
MODEL_PATH = "model.bin"
FEATURES_PATH = "feature_columns.bin"

def main():
    # Load and clean
    df = pd.read_csv(DATA_PATH)
    
    # Target encoding: 'Yes' -> 1, 'No' -> 0
    X = df.drop(columns="Attrition")
    y = (df["Attrition"].str.lower() == "yes").astype(int)

    # Imbalance calculation for XGBoost
    ratio = (y == 0).sum() / (y == 1).sum()

    # Simple One-Hot Encoding
    X = pd.get_dummies(X, drop_first=True)
    feature_names = X.columns.tolist()

    X_tr, X_val, y_tr, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    models = {
        "logreg": LogisticRegression(max_iter=1000),
        "rf": RandomForestClassifier(n_estimators=200, random_state=42),
        "xgb": XGBClassifier(
            n_estimators=300,
            max_depth=4,
            learning_rate=0.05,
            scale_pos_weight=ratio,  # Handles 'No' > 'Yes' imbalance
            eval_metric="logloss",
            random_state=42
        ),
    }

    best_auc = 0
    best_model = None

    for name, model in models.items():
        model.fit(X_tr, y_tr)
        y_pred = model.predict_proba(X_val)[:, 1]
        auc = roc_auc_score(y_val, y_pred)
        print(f"{name:10} | ROC-AUC: {auc:.4f}")

        if auc > best_auc:
            best_auc = auc
            best_model = model

    print(f"\nFinal Choice: {best_model.__class__.__name__} with AUC {best_auc:.4f}")

    # Export Artifacts
    with open(MODEL_PATH, "wb") as f_m, open(FEATURES_PATH, "wb") as f_f:
        pickle.dump(best_model, f_m)
        pickle.dump(feature_names, f_f)

if __name__ == "__main__":
    main()
