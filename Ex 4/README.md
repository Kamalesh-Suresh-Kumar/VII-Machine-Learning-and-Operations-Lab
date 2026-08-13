# Ex 4 – MLflow Model Registry

## Objective

To understand and implement MLflow Model Registry for registering, versioning, managing, and tracking machine learning models throughout their lifecycle.

---

## Software Used

- Python
- MLflow
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- Git
- GitHub
- Visual Studio Code
- PowerShell / Git Bash
- Web Browser

---

## Experiment Description

MLflow Model Registry is a centralized system used to manage the complete lifecycle of machine learning models.

It provides a structured way to register models, create different model versions, maintain model metadata, and manage models through the MLflow UI and APIs.

In this experiment, a Random Forest Classifier was trained using the Iris dataset and registered with MLflow. Model registration was performed using MLflow, and model versions and metadata were managed using the MLflow Model Registry.

---

## Procedure

### 1. Prepare the Environment

A Python virtual environment was created for the experiment.

The required packages were installed using:

```bash
pip install mlflow scikit-learn pandas matplotlib seaborn
```

The required MLflow and machine learning dependencies were successfully installed.

---

### 2. Start the MLflow Server

The MLflow tracking server was started to provide access to the MLflow Tracking and Model Registry interfaces.

The following command was used:

```bash
mlflow server --host 0.0.0.0 --port 5000
```

The MLflow interface was then accessed through:

```text
http://localhost:5000
```

---

### 3. Train the Machine Learning Model

A Random Forest Classifier was trained using the Iris dataset.

The dataset was divided into training and testing sets, and the Random Forest model was trained using the training data.

The model used:

```text
Model: Random Forest Classifier
Dataset: Iris
```

---

### 4. Register the Model

The trained Random Forest model was logged to MLflow and registered in the Model Registry.

The registered model used in the experiment was:

```text
random-forest-classifier
```

MLflow stored the model artifact and created a registered model with a model version.

---

### 5. Register the Model Using the MLflow SDK

The model was also registered programmatically using the MLflow Python SDK.

The MLflow `log_model()` functionality was used with a registered model name.

This automatically allowed MLflow to:

- Create the registered model if it did not already exist.
- Create a model version.
- Store the model artifact.
- Link the model version to the corresponding MLflow run.

---

### 6. Create Model Versions

Different versions of a registered model can be maintained using MLflow Model Registry.

Each model version represents a different iteration of the machine learning model.

The model versions maintain information such as:

- Source MLflow run
- Artifact location
- Version-specific metadata
- Tags
- Model status

Model versions can therefore be used to track different iterations of a model.

---

### 7. Manage Model Metadata

Model metadata was managed using the MLflow Model Registry.

Descriptions and tags can be associated with registered models and individual model versions.

Examples of metadata include:

```text
project_name
task
framework
```

The model can therefore be organized and identified more easily during its lifecycle.

---

### 8. View the Registered Model

The MLflow UI was opened in the browser to verify the registered model.

The **Models** section of the MLflow UI was used to view:

- Registered model
- Model versions
- Model source
- Run information
- Model metadata
- Tags

The registered Random Forest model and its version information were successfully displayed.

---

## MLflow Model Registry Workflow

The experiment workflow was:

```text
Dataset
   ↓
Train Model
   ↓
MLflow Run
   ↓
Log Model
   ↓
Register Model
   ↓
Create Model Version
   ↓
Add Metadata / Tags
   ↓
MLflow Model Registry
   ↓
View and Manage Model
```

---

## Verification

The experiment was verified by checking:

- MLflow installation
- MLflow tracking server
- Random Forest model training
- Model logging
- Registered model creation
- Model version creation
- Model metadata and tags
- Registered model in the MLflow UI

The Random Forest Classifier was successfully registered with MLflow, and the registered model and its version information could be viewed through the MLflow UI.

---

## Output

The MLflow UI displayed the registered machine learning model.

The experiment demonstrated:

```text
Registered Model:
random-forest-classifier
```

The registered model contained its associated model version and MLflow run information.

---

## Result

The Random Forest Classifier model was successfully registered and managed using MLflow Model Registry.

Model versions and metadata were successfully handled through the MLflow Model Registry and viewed using the MLflow UI.

---

## Conclusion

The experiment provided practical knowledge of MLflow Model Registry and its role in managing machine learning models.

The complete process of starting the MLflow server, training a Random Forest model, registering the model, creating model versions, managing metadata, and viewing the registered model through the MLflow UI was successfully implemented and verified.