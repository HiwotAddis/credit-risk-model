import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import get_classification_metrics

def test_get_classification_metrics():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 0, 1, 0]
    
    metrics = get_classification_metrics(y_true, y_pred)
    assert isinstance(metrics, dict)
    assert "precision" in metrics
    assert "recall" in metrics
