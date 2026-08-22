# Ex 6 – Applying CI/CD Principles to Web Development Using Jenkins, Git, and Local HTTP Server

## Objective

To implement and demonstrate Continuous Integration and Continuous Deployment (CI/CD) principles for a web application using Git, GitHub, Jenkins, and a local Python HTTP server.

The experiment demonstrates version control, source-code management, automated validation, testing, deployment, and version updates of a web application through a Jenkins pipeline.

---

## Software Used

- Jenkins
- Git
- GitHub
- Python
- HTML
- CSS
- JavaScript
- Visual Studio Code
- WSL
- PowerShell / Git Bash
- Web Browser
- Java JDK

---

## Experiment Description

CI/CD is a software development practice used to automate the process of integrating, validating, testing, and deploying application source code.

In this experiment, a simple static web application was created using HTML, CSS, and JavaScript. Git was used for version control and GitHub was used as the remote repository.

Jenkins was configured to obtain the source code from the GitHub repository and execute a CI/CD pipeline.

The Jenkins pipeline performed the following stages:

- Checkout
- Validate
- Test
- Deploy

The web application was deployed using Python's built-in HTTP server and verified through a web browser.

The experiment was implemented in two application versions. Version 1 demonstrated the initial CI/CD workflow, while Version 2 demonstrated modification of the application, Git version control, and integration of the updated version with Jenkins.

---

## Version Control and Git Operations

Git was used to maintain and track changes to the Ex 6 web application.

The Git repository was connected to the GitHub repository:

```text
https://github.com/Kamalesh-Suresh-Kumar/VII-MLOps-Lab
```

The Ex 6 files were maintained inside:

```text
Ex 6/
```

The following Git commands were practiced.

### 1. Check Repository Status

```bash
git status
```

Displays the current state of the Git working directory and staging area.

---

### 2. Add Files

```bash
git add .
```

Adds modified and newly created files to the staging area.

---

### 3. Commit Changes

```bash
git commit -m "Add Ex 6 CI/CD pipeline"
```

Creates a commit containing the staged changes.

For the Version 2 modification, a separate commit was created to maintain the version history.

---

### 4. View Commit History

```bash
git log --oneline
```

Displays the commit history of the repository in a compact format.

The commit history demonstrates the different versions of the Ex 6 application.

---

### 5. Push Changes to GitHub

```bash
git push origin main
```

Uploads the committed changes from the local repository to GitHub.

---

## Application Files

The Ex 6 web application contains the following files:

```text
Ex 6/
│
├── index.html
├── style.css
├── script.js
├── Jenkinsfile
└── README.md
```

| File | Description |
|------|-------------|
| `index.html` | Defines the structure of the web application |
| `style.css` | Defines the styling and layout of the application |
| `script.js` | Provides JavaScript-based interaction |
| `Jenkinsfile` | Defines the Jenkins CI/CD pipeline |
| `README.md` | Documents the experiment |

---

# Web Application – Version 1

The first version of the web application was created using HTML, CSS, and JavaScript.

The application contains:

- A CI/CD web application heading.
- A deployment message.
- A button for user interaction.
- CSS-based styling.
- JavaScript functionality.

The application was tested locally before integrating it with Jenkins.

---

## Local Web Application Testing – Version 1

The web application was tested using Python's built-in HTTP server.

The following command was used:

```bash
python3 -m http.server 8000 --directory "Ex 6"
```

The application was accessed through:

```text
http://localhost:8000
```

The web page was successfully displayed in the browser.

The application button was also tested to verify the JavaScript functionality.

The local testing confirmed that the Version 1 web application was working correctly before Jenkins deployment.

---

# Jenkins CI/CD Pipeline

Jenkins was used to automate the CI/CD workflow.

A Jenkins Pipeline job was created for the Ex 6 application.

### Jenkins Job

```text
Ex6-Docker-CI-CD
```

### GitHub Repository

```text
https://github.com/Kamalesh-Suresh-Kumar/VII-MLOps-Lab.git
```

### Jenkinsfile

The Jenkins pipeline definition is stored in:

```text
Ex 6/Jenkinsfile
```

The Jenkinsfile is maintained inside the GitHub repository so that the pipeline configuration is also managed through version control.

---

## Jenkins Pipeline Stages

The implemented CI/CD pipeline consists of the following stages:

```text
Checkout
   |
   v
Validate
   |
   v
Test
   |
   v
Deploy
```

---

### 1. Checkout

The Checkout stage obtains the latest source code from the GitHub repository.

The Jenkins pipeline successfully retrieved:

```text
Ex 6/Jenkinsfile
```

from the repository.

The required Git revision was checked out before continuing with the remaining pipeline stages.

---

### 2. Validate

The Validate stage checks whether the required web application files are available.

The following files were verified:

```text
Ex 6/index.html
Ex 6/style.css
Ex 6/script.js
```

The validation was completed successfully.

Output:

```text
Checking Ex 6 files...
All required files are present.
```

---

### 3. Test

The Test stage performs basic checks on the web application.

The HTML file was checked for the required HTML element, CSS link, and JavaScript elements.

The CSS and JavaScript files were also checked to ensure that they contained valid content.

Output:

```text
Testing HTML, CSS and JavaScript files...
All tests passed successfully.
```

---

### 4. Deploy

The Deploy stage starts the local Python HTTP server and deploys the Ex 6 web application.

The application was served using:

```bash
python3 -m http.server 8000 --directory "Ex 6"
```

The deployment was completed successfully.

Output:

```text
Deploying Ex 6 web application...
Web application deployed successfully.
Access URL: http://localhost:8000
```

---

# Jenkins Pipeline Execution – Version 1

The Version 1 Jenkins pipeline was executed successfully.

The complete pipeline flow was:

```text
GitHub Repository
        |
        v
Jenkins
        |
        v
Checkout
        |
        v
Validate
        |
        v
Test
        |
        v
Deploy
        |
        v
Python HTTP Server
        |
        v
Web Browser
```

The Jenkins console output confirmed that all pipeline stages were completed successfully.

---

## Jenkins Output – Version 1

### Checkout

```text
Obtained Ex 6/Jenkinsfile from git
https://github.com/Kamalesh-Suresh-Kumar/VII-MLOps-Lab.git
```

### Validate

```text
Checking Ex 6 files...
All required files are present.
```

### Test

```text
Testing HTML, CSS and JavaScript files...
All tests passed successfully.
```

### Deploy

```text
Deploying Ex 6 web application...
Web application deployed successfully.
Access URL: http://localhost:8000
```

### Final Result

```text
CI/CD pipeline completed successfully.
Finished: SUCCESS
```

---

# Version Control Workflow – Version 1

The Version 1 workflow was:

```text
Create Web Application
        |
        v
Git Repository
        |
        v
git add
        |
        v
git commit
        |
        v
git push
        |
        v
GitHub
        |
        v
Jenkins
        |
        v
CI/CD Pipeline
```

The Version 1 application and Jenkins pipeline were committed and pushed to the GitHub repository.

---

# Web Application – Version 2

Version 2 of the web application was created to demonstrate application modification and Git-based version control.

The Version 2 application was developed by modifying the existing Version 1 application.

The modifications introduced:

- A Version 2 indicator.
- An updated user interface.
- A deployment status indicator.
- Updated deployment information.
- Updated JavaScript interaction.

The Version 2 application displays:

```text
VERSION 2

CI/CD Web Application

CI/CD deployment successful!

Pipeline Deployment Active

[ Click Me ]

Deployed using Jenkins
```

---

## Version 2 JavaScript Interaction

The JavaScript functionality was updated in Version 2.

After clicking the button, the application displays:

```text
CI/CD pipeline verified successfully!
```

and:

```text
Version 2 deployed using Jenkins.
```

This confirms that the updated JavaScript functionality is working correctly.

---

# Version 2 Local Testing

The Version 2 application was tested locally using the Python HTTP server.

The command used was:

```bash
python3 -m http.server 8000 --directory "Ex 6"
```

The application was accessed through:

```text
http://localhost:8000
```

The Version 2 interface was successfully displayed in the browser.

The Version 2 button functionality was also verified.

---

# Version 2 Version-Control Workflow

The Version 2 modifications were tracked using Git.

The workflow followed was:

```text
Version 1
    |
    | Modify HTML, CSS and JavaScript
    v
Version 2
    |
    | git status
    v
Modified Files
    |
    | git add
    v
Staging Area
    |
    | git commit
    v
New Git Version
    |
    | git push
    v
GitHub Repository
    |
    v
Jenkins
    |
    v
New CI/CD Build
```

The Version 2 changes were committed separately from Version 1 to demonstrate Git version control.

---

## Version 2 Git Operations

The modified Version 2 files were staged using:

```bash
git add "Ex 6/index.html" "Ex 6/style.css" "Ex 6/script.js" "Ex 6/README.md"
```

The Version 2 changes were committed using:

```bash
git commit -m "Update Ex 6 application to Version 2"
```

The commit history was verified using:

```bash
git log --oneline -3
```

The updated version was pushed to GitHub using:

```bash
git push origin main
```

---

# Version History

Git was used to maintain separate versions of the Ex 6 application.

| Version | Description | Status |
|---------|-------------|--------|
| Version 1 | Initial web application and Jenkins CI/CD pipeline | Successfully completed |
| Version 2 | Updated web application with modified UI and JavaScript functionality | Successfully committed and pushed |

The Git commit history provides a record of the changes between Version 1 and Version 2.

---

# Version 2 CI/CD Workflow

After Version 2 was pushed to GitHub, Jenkins was used to process the updated source code.

The updated CI/CD workflow was:

```text
Version 2 Changes
        |
        v
Git Commit
        |
        v
Git Push
        |
        v
GitHub
        |
        v
Jenkins
        |
        v
Checkout
        |
        v
Validate
        |
        v
Test
        |
        v
Deploy
        |
        v
Version 2 Web Application
```

The updated source code was retrieved by Jenkins and processed through the same CI/CD stages.

---

# CI/CD Workflow

The complete workflow implemented during the experiment was:

```text
Developer
    |
    v
Web Application
    |
    v
Git Version Control
    |
    | git push
    v
GitHub Repository
    |
    v
Jenkins
    |
    +----------------+
    |                |
    v                v
 Checkout         Validate
    |                |
    +-------+--------+
            |
            v
          Test
            |
            v
          Deploy
            |
            v
 Python HTTP Server
            |
            v
      Web Browser
```

---

# Verification

The experiment was verified by checking:

- Successful creation of the Version 1 web application.
- Successful local browser testing.
- Successful Git repository configuration.
- Successful GitHub repository connection.
- Successful source-code push to GitHub.
- Successful Jenkins repository checkout.
- Successful Jenkinsfile retrieval.
- Successful application file validation.
- Successful application testing.
- Successful application deployment.
- Successful access through the local HTTP server.
- Successful Version 2 application modification.
- Successful Version 2 local browser testing.
- Successful Version 2 Git commit.
- Successful Version 2 push to GitHub.
- Successful Jenkins processing of the updated source code.
- Successful CI/CD pipeline execution.

---

# Output

The important outputs obtained during the experiment included:

### Local Web Application

```text
http://localhost:8000
```

The web application was successfully displayed in the browser.

### Jenkins Validation

```text
All required files are present.
```

### Jenkins Testing

```text
All tests passed successfully.
```

### Jenkins Deployment

```text
Web application deployed successfully.
Access URL: http://localhost:8000
```

### Jenkins Final Status

```text
Finished: SUCCESS
```

### Version 2 Application

```text
VERSION 2

CI/CD Web Application

CI/CD deployment successful!

Pipeline Deployment Active
```

After clicking the button:

```text
CI/CD pipeline verified successfully!

Version 2 deployed using Jenkins.
```

---

# Result

A CI/CD pipeline for the web application was successfully implemented using Git, GitHub, Jenkins, and a local Python HTTP server.

Version 1 of the application was successfully created, version controlled, tested, and deployed using Jenkins.

Version 2 was then created by modifying the application interface and JavaScript functionality.

The Version 2 changes were committed separately using Git and pushed to the GitHub repository.

The updated source code was integrated with the Jenkins CI/CD workflow and successfully processed through the Checkout, Validate, Test, and Deploy stages.

The web application was successfully accessed through the local browser.

---

# Conclusion

The experiment provided practical knowledge of CI/CD principles for web development.

Git and GitHub were used for source-code version control and maintaining application history, while Jenkins was used to automate the checkout, validation, testing, and deployment stages.

Version 1 demonstrated the basic CI/CD workflow, while Version 2 demonstrated how application changes can be tracked as a new Git version and integrated into the CI/CD pipeline.

The experiment successfully demonstrated the complete workflow:

```text
Version Control
       |
       v
GitHub
       |
       v
Jenkins
       |
       v
Checkout
       |
       v
Validate
       |
       v
Test
       |
       v
Deploy
       |
       v
Web Application
```

The successful execution of the CI/CD pipeline demonstrates the practical application of version control and automated software delivery.