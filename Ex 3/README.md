# Ex 3 – Experiment Tracking Using MLflow

## Objective

To understand and implement experiment tracking using MLflow by creating experiments, recording parameters and metrics, and viewing experiment results through the MLflow UI.

---

## Software Used

- Python
- MLflow
- Git
- GitHub
- Visual Studio Code
- PowerShell / Git Bash
- Web Browser

---

## Experiment Description

MLflow is an open-source platform used to manage and track the machine learning lifecycle.

In this experiment, MLflow was installed and configured to track machine learning experiments. Parameters and performance metrics were logged during an MLflow run, and the recorded experiment was viewed using the MLflow user interface.

MLflow Tracking records information such as parameters, metrics, and artifacts generated during machine learning runs. It also allows different runs to be organized and compared.

---

## Procedure

### 1. Install MLflow

MLflow was installed using Python's package manager.

The following command was used:

```bash
pip install mlflow
```

The installation was completed successfully.

---

### 2. Create an MLflow Experiment

An MLflow experiment was created using the experiment name:

```text
MLflow Quickstart
```

The experiment was configured using MLflow's experiment tracking functionality.

---

### 3. Start an MLflow Run

An MLflow run was created to record information related to the experiment.

During the run, parameters and metrics were logged.

The experiment demonstrated logging:

```text
Parameter:
learning_rate = 0.01

Metric:
accuracy = 0.95
```

The run was successfully recorded by MLflow.

---

### 4. Track Experiment Information

MLflow Tracking was used to record information generated during the experiment.

The tracked information included:

- Parameters
- Metrics
- Experiment runs
- Artifacts
- Run information

MLflow Tracking provides a way to organize experiments and compare different training runs.

---

### 5. Start the MLflow UI

The MLflow user interface was started to view the recorded experiments.

The following command was used:

```bash
mlflow ui
```

MLflow generated a local address that could be opened in a web browser to access the interface.

---

### 6. View the Experiment

The MLflow UI was opened in the browser.

The experiment and its recorded run were viewed through the MLflow interface.

The tracking server was accessed using:

```text
http://localhost:5000
```

The recorded experiment, parameters, metrics, and run information were displayed in the MLflow UI.

---

## MLflow Tracking Workflow

The experiment workflow was:

```text
Python Application
       ↓
MLflow Experiment
       ↓
MLflow Run
       ↓
Log Parameters and Metrics
       ↓
MLflow Tracking
       ↓
MLflow UI
       ↓
View and Compare Results
```

---

## Verification

The experiment was verified by checking:

- MLflow installation
- Creation of the MLflow experiment
- Successful creation of an MLflow run
- Parameter logging
- Metric logging
- MLflow UI execution
- Display of the experiment in the MLflow UI

The experiment successfully recorded the parameter `learning_rate` and the metric `accuracy` during the MLflow run.

---

## Output

The MLflow UI successfully displayed the recorded experiment and run information.

The following values were recorded during the experiment:

```text
learning_rate = 0.01
accuracy = 0.95
```

The MLflow UI was accessed through the local browser interface at:

```text
http://localhost:5000
```

---

## Result

MLflow was successfully installed and configured for experiment tracking.

An MLflow experiment and run were created successfully, parameters and metrics were logged, and the experiment results were viewed through the MLflow UI.

---

## Conclusion

The experiment provided practical knowledge of MLflow experiment tracking.

The complete process of installing MLflow, creating an experiment, logging parameters and metrics, starting the MLflow UI, and viewing the recorded experiment was successfully implemented and verified.