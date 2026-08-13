# Ex 2 – Implementing a CI/CD Pipeline with Jenkins

## Objective

To implement a Continuous Integration and Continuous Delivery (CI/CD) pipeline using Jenkins for automatically building and testing a Maven-based Java application.

---

## Software Used

- Java JDK
- Jenkins
- Git
- GitHub
- Apache Maven
- Visual Studio Code
- PowerShell / Git Bash

---

## Experiment Description

Jenkins is an automation server used to automate software development processes such as building, testing, and deploying applications.

In this experiment, Jenkins was installed and configured, connected with a GitHub repository, and used to create a CI/CD pipeline for a Maven-based Java application.

The pipeline was used to automatically obtain the source code, build the application, execute the test cases, and verify the build result.

---

## Procedure

### 1. Install Java

Java JDK was installed and configured as a prerequisite for Jenkins and Maven.

The Java installation was verified using the following command:

```bash
java --version
```

---

### 2. Install Jenkins

Jenkins was downloaded and installed on the system.

After installation, the Jenkins service was started and accessed through:

```text
http://localhost:8080
```

The initial Jenkins setup was completed by unlocking Jenkins, installing the required plugins, and creating the administrator account.

---

### 3. Configure Jenkins

The required tools and plugins were configured in Jenkins.

Git and Maven were configured so that Jenkins could obtain the source code and build the Java application.

---

### 4. Connect GitHub Repository

The Maven project was maintained in a GitHub repository.

The GitHub repository was connected to Jenkins so that Jenkins could obtain the latest source code for the CI/CD pipeline.

---

### 5. Create Jenkins Pipeline

A Jenkins Pipeline was created for the project.

The pipeline consisted of the following stages:

1. Checkout
2. Build
3. Test
4. Deploy

The pipeline automatically executed the required steps whenever the job was triggered.

---

### 6. Build the Application

Maven was used to build the Java application.

The following command was executed during the build stage:

```bash
mvn clean package
```

The application was successfully compiled and packaged.

The generated JAR file was:

```text
mlops-ci-1.0-SNAPSHOT.jar
```

---

### 7. Execute Tests

The project tests were executed using:

```bash
mvn test
```

The test execution was successful.

The result was:

```text
Tests run: 1
Failures: 0
Errors: 0
Skipped: 0
```

---

### 8. Verify Jenkins Build

The Jenkins console output was checked to verify the successful execution of the pipeline.

The final build result was:

```text
BUILD SUCCESS
```

The pipeline successfully completed the Build, Test, and Deploy stages.

---

## CI/CD Workflow

The implemented workflow was:

```text
GitHub
   ↓
Jenkins
   ↓
Checkout
   ↓
Build
   ↓
Test
   ↓
Deploy
   ↓
Successful Pipeline
```

---

## Verification

The experiment was verified by checking:

- Jenkins installation and configuration
- GitHub repository connection
- Source code checkout
- Maven build execution
- Maven test execution
- Generated JAR file
- Successful Jenkins pipeline execution

The Jenkins build successfully generated the application JAR file and reported `BUILD SUCCESS`.

The test stage also completed with one test executed and no failures or errors.

---

## Output

The Jenkins console displayed the successful execution of the Maven build and testing process.

The generated artifact was:

```text
mlops-ci-1.0-SNAPSHOT.jar
```

Final build status:

```text
BUILD SUCCESS
```

Screenshots of the Jenkins pipeline and successful build execution are included in the `outputs` folder.

---

## Result

A CI/CD pipeline was successfully implemented using Jenkins.

The GitHub repository was connected to Jenkins, and the Maven application was successfully built and tested through the Jenkins pipeline.

---

## Conclusion

The experiment provided practical knowledge of Jenkins-based CI/CD automation.

The complete process of integrating GitHub with Jenkins and automatically building and testing a Maven application was successfully implemented and verified.