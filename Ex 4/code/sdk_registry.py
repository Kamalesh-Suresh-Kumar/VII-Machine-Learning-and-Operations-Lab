import mlflow
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

TRACKING_URI = "http://localhost:5000"
MODEL_SDK_NAME = "registered-model-sdk"

mlflow.set_tracking_uri(TRACKING_URI)
client = MlflowClient()


def train_fit_model(n_estimators=50, random_state=42):
    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=random_state
    )

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model


def sdk_auto_register():
    model = train_fit_model(80)

    with mlflow.start_run(run_name="sdk-auto-register") as run:

        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="RandomForestClassifier",
            registered_model_name=MODEL_SDK_NAME
        )

        print(
            f"[SDK] Auto-registered under '{MODEL_SDK_NAME}' "
            f"with run_id={run.info.run_id}"
        )


sdk_auto_register()