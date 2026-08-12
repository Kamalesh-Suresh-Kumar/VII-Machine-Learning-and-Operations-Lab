import mlflow
from pathlib import Path

db_path = Path(__file__).resolve().parent.parent / "mlflow.db"
mlflow.set_tracking_uri("sqlite:///" + db_path.as_posix())

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)

print("Run logged successfully!")