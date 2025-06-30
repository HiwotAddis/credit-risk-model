from sklearn.metrics import precision_score, recall_score, f1_score


def get_classification_metrics(y_true, y_pred):
    return {
        "precision": round(precision_score(y_true, y_pred), 2),
        "recall": round(recall_score(y_true, y_pred), 2),
        "f1_score": round(f1_score(y_true, y_pred), 2),
    }
