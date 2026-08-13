# Ex 1 – Exploring Git Commands Through Collaborative Coding

## Objective

To explore and practice Git commands used for version control, repository management, branching, committing changes, and collaborating with GitHub.

---

## Software Used

- Git
- GitHub
- Git Bash / PowerShell
- Visual Studio Code

---

## Experiment Description

Git is a distributed version control system used to track changes made to files and manage different versions of a project.

In this experiment, the basic Git workflow was explored by creating and managing a repository, checking repository status, staging files, committing changes, working with branches, connecting the local repository with GitHub, and pushing changes to the remote repository.

---

## Git Commands Used

### 1. Initialize Repository

```bash
git init
```

Initializes a new Git repository in the current directory.

---

### 2. Check Repository Status

```bash
git status
```

Displays the current state of the working directory and staging area.

---

### 3. Add Files to Staging Area

```bash
git add .
```

Stages all modified and newly created files for the next commit.

---

### 4. Commit Changes

```bash
git commit -m "Initial commit"
```

Creates a commit containing the staged changes.

---

### 5. View Branches

```bash
git branch
```

Displays the available branches in the local repository.

---

### 6. Create a New Branch

```bash
git branch feature
```

Creates a new branch named `feature`.

---

### 7. Switch Branch

```bash
git checkout feature
```

Switches from the current branch to the `feature` branch.

---

### 8. View Remote Repository

```bash
git remote -v
```

Displays the remote repositories connected to the local Git repository.

---

### 9. Push Changes

```bash
git push origin main
```

Uploads the local commits from the `main` branch to the remote GitHub repository.

---

### 10. Pull Changes

```bash
git pull origin main
```

Downloads and integrates the latest changes from the remote `main` branch.

---

### 11. View Commit History

```bash
git log
```

Displays the commit history of the repository.

---

## Basic Git Workflow

```text
Working Directory
       |
       | git add
       v
Staging Area
       |
       | git commit
       v
Local Repository
       |
       | git push
       v
GitHub Repository
```

---

## Git and GitHub Workflow

The following workflow was followed during the experiment:

1. Created or initialized a local Git repository.
2. Checked the repository status.
3. Added files to the staging area.
4. Committed the changes.
5. Created and worked with branches.
6. Connected the local repository with GitHub.
7. Pushed the committed changes to the remote repository.
8. Pulled changes from GitHub when required.
9. Viewed the commit history using Git commands.

---

## Result

The basic Git commands were successfully explored and practiced.

The local repository was successfully connected with GitHub, and the changes were committed and pushed to the remote repository.

---

## Conclusion

The experiment provided practical knowledge of Git version control and demonstrated the basic workflow used to manage source code and collaborate through GitHub.