import mlflow
import mlflow.sklearn

from pathlib import Path

db_path = Path(__file__).resolve().parent.parent / "mlflow.db"
mlflow.set_tracking_uri("sqlite:///" + db_path.as_posix())

mlflow.autolog()

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

mlflow.sklearn.autolog()

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

print("Model trained successfully!")