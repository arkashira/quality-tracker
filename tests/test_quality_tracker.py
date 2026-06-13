import pytest
from src.quality_tracker import QualityTracker, QualityMetric
import datetime

def test_collect_metrics():
    tracker = QualityTracker()
    tracker.collect_metrics()
    assert len(tracker.metrics) > 0

def test_visualize_metrics(capsys):
    tracker = QualityTracker()
    tracker.collect_metrics()
    tracker.visualize_metrics()
    captured = capsys.readouterr()
    assert "Visualizing metrics:" in captured.out

def test_quality_metric():
    metric = QualityMetric("Test Metric", 50.0, datetime.datetime.now())
    assert metric.name == "Test Metric"
    assert metric.value == 50.0
    assert isinstance(metric.timestamp, datetime.datetime)
