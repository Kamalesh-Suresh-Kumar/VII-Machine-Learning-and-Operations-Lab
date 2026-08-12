import mlflow
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

TRACKING_URI = "http://localhost:5000"
REGISTERED_MODEL_NAME = "random-forest-classifier"

mlflow.set_tracking_uri(TRACKING_URI)
client = MlflowClient()

# Load and split data
X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
clf = RandomForestClassifier(n_estimators=120, random_state=42)
clf.fit(X_train, y_train)

# Log model and auto-register
with mlflow.start_run(run_name="rf-iris-single-file") as run:

    mlflow.log_param("n_estimators", 120)
    mlflow.log_param("random_state", 42)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    mlflow.log_metric("accuracy", acc)

    mlflow.sklearn.log_model(
        sk_model=clf,
        artifact_path="RandomForestClassifier",
        registered_model_name=REGISTERED_MODEL_NAME
    )

print("Model registered successfully!")
print("Accuracy:", acc)