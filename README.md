# VII – Machine Learning and Operations Lab

## Laboratory Experiments

This repository contains the practical experiments performed as part of the **VII – Machine Learning and Operations Lab**.

The experiments provide hands-on experience with software version control, continuous integration and delivery, machine learning experiment tracking, model lifecycle management, and containerization.

---

## Course Overview

Machine Learning Operations (MLOps) combines machine learning development with software engineering and operational practices to make machine learning systems reliable, reproducible, maintainable, and deployable.

This laboratory focuses on the fundamental tools and workflows used in an MLOps environment.

The experiments progressively introduce the major stages of an MLOps workflow:

```text
Version Control
      ↓
CI/CD Automation
      ↓
Experiment Tracking
      ↓
Model Registry
      ↓
Containerization
```

---

## Overall Experiment Structure

| Experiment | Title | Primary Tool / Technology | Main Concept |
|---|---|---|---|
| Ex 1 | Exploring Git Commands Through Collaborative Coding | Git, GitHub | Version Control |
| Ex 2 | Implementing a CI/CD Pipeline with Jenkins | Jenkins, Maven, GitHub | Continuous Integration and Delivery |
| Ex 3 | Experiment Tracking Using MLflow | MLflow | Experiment Tracking |
| Ex 4 | MLflow Model Registry | MLflow | Model Versioning and Lifecycle Management |
| Ex 5 | Docker Installation and Verification | Docker Desktop | Containerization |

---

## Experiment 1 – Exploring Git Commands Through Collaborative Coding

### Objective

To explore and practice Git commands used for version control, repository management, branching, committing changes, and collaboration with GitHub.

### Key Concepts

- Git repository management
- Working directory
- Staging area
- Commits
- Branches
- Remote repositories
- GitHub
- Push and pull operations
- Version control workflow

### Outcome

The basic Git workflow was implemented and practiced by creating a repository, tracking changes, committing files, working with branches, connecting the repository with GitHub, and pushing changes to the remote repository.

---

## Experiment 2 – Implementing a CI/CD Pipeline with Jenkins

### Objective

To implement a Continuous Integration and Continuous Delivery (CI/CD) pipeline using Jenkins for automatically building and testing a Maven-based Java application.

### Key Concepts

- Jenkins
- Continuous Integration
- Continuous Delivery
- GitHub integration
- Maven
- Automated builds
- Automated testing
- Jenkins Pipeline

### Outcome

A Jenkins-based CI/CD pipeline was successfully configured and connected with a GitHub repository.

The Maven application was successfully built and tested through Jenkins, producing a successful build result.

---

## Experiment 3 – Experiment Tracking Using MLflow

### Objective

To understand and implement experiment tracking using MLflow by creating experiments, recording parameters and metrics, and viewing experiment results through the MLflow UI.

### Key Concepts

- MLflow
- Experiment tracking
- MLflow runs
- Parameters
- Metrics
- Artifacts
- MLflow UI
- Experiment comparison

### Outcome

MLflow was successfully installed and configured.

An experiment and run were created, parameters and metrics were recorded, and the experiment results were viewed through the MLflow UI.

---

## Experiment 4 – MLflow Model Registry

### Objective

To understand and implement MLflow Model Registry for registering, versioning, managing, and tracking machine learning models throughout their lifecycle.

### Key Concepts

- MLflow Model Registry
- Model registration
- Model versions
- Model metadata
- Model tags
- Model lifecycle management
- MLflow UI
- Model management using the MLflow SDK

### Outcome

A machine learning model was successfully registered using MLflow Model Registry.

Model versions and associated metadata were managed and viewed through the MLflow interface.

---

## Experiment 5 – Docker Installation and Verification

### Objective

To install Docker Desktop on Windows and verify that the Docker environment is working correctly by running the Docker `hello-world` container.

### Key Concepts

- Docker Desktop
- Docker Engine
- Docker images
- Docker containers
- Docker Hub
- Container execution
- Docker Compose

### Outcome

Docker Desktop was successfully installed and configured on Windows.

The installation was verified using Docker commands, and the official `hello-world` container was successfully executed.

---

## Overall MLOps Workflow

The experiments together demonstrate a basic end-to-end MLOps workflow:

```text
┌──────────────────────────────┐
│          Git / GitHub        │
│       Version Control        │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│           Jenkins            │
│        CI/CD Pipeline        │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│           MLflow             │
│     Experiment Tracking      │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│      MLflow Model Registry   │
│    Model Version Management  │
└──────────────┬───────────────┘
               │
               ↓
┌──────────────────────────────┐
│            Docker            │
│        Containerization      │
└──────────────────────────────┘
```

---

## Technologies Covered

| Category | Technologies |
|---|---|
| Version Control | Git, GitHub |
| CI/CD | Jenkins |
| Build Automation | Apache Maven |
| Programming | Python, Java |
| Experiment Tracking | MLflow |
| Model Management | MLflow Model Registry |
| Containerization | Docker |
| Container Platform | Docker Desktop |
| Development Environment | Visual Studio Code |
| Operating System | Windows, WSL |

---

## Learning Outcomes

After completing these experiments, the following practical skills were developed:

- Understanding Git-based version control.
- Managing source code using GitHub.
- Creating and managing branches.
- Performing commits, pushes, and pulls.
- Understanding Continuous Integration and Continuous Delivery.
- Configuring Jenkins for automated builds.
- Integrating GitHub with Jenkins.
- Building and testing Maven-based applications.
- Tracking machine learning experiments using MLflow.
- Recording parameters and metrics.
- Managing machine learning models using MLflow Model Registry.
- Understanding model versioning and metadata.
- Installing and configuring Docker Desktop.
- Working with Docker images and containers.
- Verifying a Docker installation using the `hello-world` container.
- Understanding the relationship between development, automation, experiment tracking, model management, and deployment environments.

---

## Repository Structure

The repository is organized according to the laboratory experiments.

| Directory | Description |
|---|---|
| `Ex 1` | Git and GitHub version control experiment |
| `Ex 2` | Jenkins CI/CD pipeline experiment |
| `Ex 3` | MLflow experiment tracking |
| `Ex 4` | MLflow Model Registry |
| `Ex 5` | Docker installation and verification |

Each experiment contains its own README file describing the objective, software used, procedure, verification, output, result, and conclusion.

---

## Final Result

All five laboratory experiments were successfully completed.

The laboratory provided practical exposure to the core tools and workflows used in MLOps, beginning with source-code management and progressing through CI/CD automation, machine learning experiment tracking, model lifecycle management, and containerization.

The completed experiments establish a foundation for implementing more advanced MLOps workflows involving automated model training, deployment, monitoring, and scalable machine learning systems.

---

## Future Scope

The completed experiments establish the foundation of an MLOps workflow through Git, Jenkins, MLflow, MLflow Model Registry, and Docker.

The upcoming experiments will extend this foundation toward more advanced DevOps and MLOps practices, covering containerized CI/CD, Kubernetes orchestration, cloud-based automation, deployment strategies, and application security testing.

### Planned Future Experiments

| Area | Planned Experiment | Focus |
|---|---|---|
| Git & GitHub | Implement GitHub Operations | Remote repository management, collaboration, and GitHub-based workflows |
| CI/CD | CI/CD for Web Development using Jenkins, Git and Local HTTP Server | Automated build, testing, and deployment of web applications |
| Containerization | Application Deployment with Docker | Building Docker images and deploying applications using containers |
| Containerized CI/CD | Jenkins, Git and Docker Containers | Integrating Jenkins CI/CD with Docker-based application deployment |
| Container Orchestration | Container Orchestration using Kubernetes | Managing containers, deployments, services, scaling, and orchestration |
| Cloud CI/CD | CI/CD Pipeline using Cloud Platform | Implementing cloud-based CI/CD workflows using GitHub and cloud services |
| Deployment Strategy | Blue-Green Deployment | Reducing application downtime and enabling safer application releases |
| Security & Testing | Testing using OWASP ZAP and Postman | API testing, security testing, vulnerability detection, and application validation |

### Future MLOps Progression

The planned experiments will extend the current workflow as follows:

```text
Git / GitHub
      ↓
Jenkins CI/CD
      ↓
Docker
      ↓
Jenkins + Docker
      ↓
Kubernetes
      ↓
Cloud CI/CD
      ↓
Blue-Green Deployment
      ↓
API Testing
      ↓
Security Testing
```

---

## Author

**Kamalesh Suresh Kumar**