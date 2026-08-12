import mlflow
from mlflow.tracking import MlflowClient

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


TRACKING_URI = "http://localhost:5000"

mlflow.set_tracking_uri(TRACKING_URI)

client = MlflowClient()


def train_fit_model(n_estimators=50, random_state=42):

    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=random_state
    )

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model


def canonical_flow_with_versions_tags_aliases():

    registered_model_name = "random-forest-classifier-lab"

    # --------------------------------------------------
    # Ensure registered model exists
    # --------------------------------------------------

    try:
        client.get_registered_model(registered_model_name)

    except Exception:
        client.create_registered_model(registered_model_name)

    # --------------------------------------------------
    # Version A
    # --------------------------------------------------

    modelA = train_fit_model(60)

    with mlflow.start_run(run_name="canonical-A") as runA:

        mlflow.sklearn.log_model(
            sk_model=modelA,
            artifact_path="RandomForestClassifier",
            registered_model_name=registered_model_name
        )

        runA_id = runA.info.run_id

    # --------------------------------------------------
    # Update registered model description
    # --------------------------------------------------

    client.update_registered_model(
        name=registered_model_name,
        description="Canonical RF classifier lab model"
    )

    # --------------------------------------------------
    # Find Version A
    # --------------------------------------------------

    versions_A = client.search_model_versions(
        f"name = '{registered_model_name}' and run_id = '{runA_id}'"
    )

    vA = versions_A[0].version

    # --------------------------------------------------
    # Update Version A description
    # --------------------------------------------------

    client.update_model_version(
        name=registered_model_name,
        version=vA,
        description="Version A: n_estimators=60"
    )

    # --------------------------------------------------
    # Set registered model tags
    # --------------------------------------------------

    tags = {
        "project_name": "UNDERFINED",
        "task": "classification",
        "framework": "sklearn"
    }

    for k, v in tags.items():

        client.set_registered_model_tag(
            name=registered_model_name,
            key=k,
            value=v
        )

    # --------------------------------------------------
    # Set aliases for Version A
    # --------------------------------------------------

    for alias in ["development", "candidate", "Champion"]:

        client.set_registered_model_alias(
            name=registered_model_name,
            alias=alias,
            version=vA
        )

    print(f"Version A created: v{vA}")

    # --------------------------------------------------
    # Version B
    # --------------------------------------------------

    modelB = train_fit_model(120)

    with mlflow.start_run(run_name="canonical-B") as runB:

        mlflow.sklearn.log_model(
            sk_model=modelB,
            artifact_path="RandomForestClassifier"
        )

        mvB = client.create_model_version(
            name=registered_model_name,
            source=runB.info.artifact_uri,
            run_id=runB.info.run_id,
            description="Version B: n_estimators=120"
        )

    # --------------------------------------------------
    # Move Champion alias to Version B
    # --------------------------------------------------

    client.set_registered_model_alias(
        name=registered_model_name,
        alias="Champion",
        version=mvB.version
    )

    print(f"Version B created: v{mvB.version}")

    print()
    print("Canonical workflow completed successfully!")
    print(f"Registered Model: {registered_model_name}")
    print(f"Version A: v{vA}")
    print(f"Version B: v{mvB.version}")
    print("Champion -> Version B")


if __name__ == "__main__":

    canonical_flow_with_versions_tags_aliases()