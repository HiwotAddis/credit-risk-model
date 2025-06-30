import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils import get_classification_metrics


def test_get_classification_metrics():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 0, 1, 0]

    metrics = get_classification_metrics(y_true, y_pred)
    assert isinstance(metrics, dict)
    assert "precision" in metrics
    assert "recall" in metrics


def test_metrics_all_correct():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 1, 0]  # perfect prediction
    metrics = get_classification_metrics(y_true, y_pred)

    assert metrics["precision"] == 1.0
    assert metrics["recall"] == 1.0
    assert metrics["f1_score"] == 1.0


def test_metrics_partial_correct():
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]
    metrics = get_classification_metrics(y_true, y_pred)

    assert isinstance(metrics, dict)
    assert 0 <= metrics["precision"] <= 1
    assert 0 <= metrics["recall"] <= 1
    assert 0 <= metrics["f1_score"] <= 1
