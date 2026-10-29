# Student Marks Analyzer — DevOps & Data Drift Monitoring

A Python-based Student Marks Analyzer integrated with a DevOps pipeline using GitHub, Jenkins, Docker, Pytest, and Evidently AI. The project demonstrates automated testing, containerization, continuous integration, and data drift monitoring through an HTML report.

## 1. Project Objectives

- Develop a Python application to calculate student average marks and determine Pass/Fail status.
- Maintain source code using Git and GitHub.
- Automate application testing using Pytest.
- Package and run the application using Docker.
- Automate the development workflow using Jenkins.
- Monitor data drift using Evidently AI.
- Generate an HTML report containing data drift analysis.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Git and GitHub | Version control and source code hosting |
| Jenkins | Continuous Integration (CI) pipeline |
| Docker | Application containerization |
| Pytest | Automated testing |
| Evidently AI | Data drift monitoring |
| Pandas | Data handling |
| SciPy | Statistical computations used by monitoring dependencies |
| HTML | Monitoring report output |
| Ubuntu Linux | Development environment |

## 3. Project Structure

```text
student-marks-demo/
│
├── hello.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
├── tests/
│   └── test_hello.py
│
├── monitoring/
│   ├── data_drift.py
│   ├── drift_report.html
│   └── reports/
│       └── drift_report.html
│
└── README.md
```

**Note:** The HTML report files are generated outputs. The `monitoring/reports/drift_report.html` file is the expected output path used by the Jenkins pipeline.

## 4. Prerequisites

Install or configure the following before running the project:

- Ubuntu Linux or another compatible operating system.
- Python 3.12 and pip.
- Git.
- Docker Engine.
- Jenkins with Pipeline support.
- Internet access for installing Python packages and retrieving the repository.
- A GitHub account if you want to push changes to your own repository.

Verify the main tools:

```bash
python3 --version
git --version
docker --version
```

Check Jenkins at:

```text
http://localhost:8080
```

## 5. Clone the Repository

Open a terminal and navigate to the directory where you want to store the project.

```bash
git clone https://github.com/Atharv-1905/student-marks-demo.git
cd student-marks-demo
```

## 6. Set Up the Python Environment

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the dependencies used by the project, including Pytest, Pandas, and Evidently.

## 7. Run the Python Application

From the project root, execute:

```bash
python hello.py
```

Expected output:

```text
Student Marks Analyzer
Marks: [75, 80, 65]
Average: 73.33333333333333
Result: Pass
```

The application calculates the average of the supplied marks and determines whether the student passes or fails based on the configured threshold of 40.

## 8. Run Automated Tests Using Pytest

Execute the tests from the project root:

```bash
python -m pytest -v
```

The test suite checks the application's marks analysis logic.

Expected result:

```text
tests/test_hello.py::test_student_pass PASSED
```

A successful test run confirms that the implemented test case passes.

## 9. Build the Docker Image

Make sure Docker Engine is running.

Build the project image:

```bash
docker build -t student-marks-demo:2.0 .
```

Check the available image:

```bash
docker images student-marks-demo
```

The Dockerfile uses Python 3.12 slim as its base image, installs the required dependencies, and copies the application, tests, and monitoring source files into the container.

## 10. Run the Application Inside Docker

Execute:

```bash
docker run --rm student-marks-demo:2.0
```

The application should print the marks, calculated average, and result.

The `--rm` option automatically removes the stopped container after execution.

## 11. Run Pytest Inside Docker

Execute:

```bash
docker run --rm student-marks-demo:2.0 python -m pytest -v
```

This verifies that the tests can also run inside the Docker environment.

## 12. Run Evidently Data Drift Monitoring

The monitoring script compares reference data with current data to identify potential data drift.

First, create the report directory:

```bash
mkdir -p monitoring/reports
```

Run the monitoring script from the project root:

```bash
python monitoring/data_drift.py
```

Alternatively, run it inside Docker:

```bash
docker run --rm \
  -v "$PWD/monitoring/reports:/app/monitoring/reports" \
  student-marks-demo:2.0 \
  python monitoring/data_drift.py
```

The mounted volume allows the generated report to remain on the host machine after the container exits.

Verify the report:

```bash
ls -lh monitoring/reports/drift_report.html
```

Open it in your default browser:

```bash
xdg-open monitoring/reports/drift_report.html
```

The HTML report can be used to inspect the results of the data drift analysis.

## 13. Jenkins CI Pipeline

The Jenkins pipeline automates the project's main validation and monitoring stages.

### Pipeline stages

1. **Pull Code from GitHub:** Retrieves the latest code from the `main` branch.
2. **Setup Python:** Creates a Python virtual environment and installs Pytest.
3. **Run Tests:** Executes the automated test suite.
4. **Docker Build:** Builds the application image.
5. **Docker Application Test:** Runs the application inside the container.
6. **Docker Pytest:** Executes tests inside Docker.
7. **Evidently Monitoring:** Runs data drift monitoring and generates the HTML report.
8. **Archive Artifacts:** Archives the report after a successful pipeline run.

### Configure Jenkins

1. Open Jenkins at `http://localhost:8080`.
2. Create or open the Pipeline job named `student-marks-pipeline`.
3. Configure the job to retrieve code from the GitHub repository.
4. Select the `main` branch.
5. Add the project's Jenkins Pipeline script in the Pipeline configuration.
6. Save the configuration.
7. Click **Build Now**.
8. Open the build's **Console Output** to inspect the stages.

The Jenkins service account must have the required Docker permissions to execute Docker commands.

### Expected result

A successful pipeline should finish with:

```text
SUCCESS: All CI stages completed!
Jenkins pipeline execution finished.
Finished: SUCCESS
```

After a successful build, open its page and locate the archived HTML report under **Build Artifacts**.

Download the report and open it locally in Chrome or Firefox if the browser displays the HTML source when accessed directly through Jenkins.

## 14. Git Workflow

Check the working tree:
x
```bash
git status
```

Stage changes:

```bash
git add .
```

Commit the changes:

```bash
git commit -m "Update project documentation and monitoring"
```

Push to GitHub:

```bash
git push origin main
```

If Git requests authentication, use an appropriate GitHub authentication method, such as SSH or a personal access token, rather than your GitHub account password.

## 15. Troubleshooting

### A. Python dependency errors

Activate the virtual environment and reinstall dependencies:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### B. Docker permission errors

Verify that Docker is available:

```bash
docker version
```

If permission is denied, check Docker service status and the permissions of the current user. Adding a user to the Docker group grants powerful privileges equivalent to root access, so do so only when appropriate.

### C. Jenkins cannot execute Docker

Check that the Jenkins service account can access Docker. Restart Jenkins after making any required service-account group changes.

### D. HTML report is missing

Create the expected output directory:

```bash
mkdir -p monitoring/reports
```

Check that `monitoring/data_drift.py` saves the report to:

```text
monitoring/reports/drift_report.html
```

Ensure that the directory is mounted when running the monitoring script inside a temporary Docker container.

### E. Jenkins pipeline fails

Open the failed build and inspect **Console Output**. Identify the first failed stage before changing the configuration.

### F. HTML source appears in the browser

Download the report from Jenkins and open the downloaded file locally in Chrome or Firefox.

## 16. Limitations

- The application uses a small, predefined set of student marks.
- The included test suite covers only the implemented test cases.
- The monitoring script uses sample reference and current datasets rather than a live production data stream.
- Data drift detection indicates changes in the input data distribution; it does not by itself prove that model performance has deteriorated.
- The Jenkins workflow requires a configured Jenkins server and Docker access.

## 17. Future Enhancements

- Add a command-line interface for entering student marks.
- Expand the test suite to cover invalid, empty, and boundary-value inputs.
- Integrate a larger dataset for more representative drift analysis.
- Add automated monitoring alerts when drift is detected.
- Publish the HTML report through a dedicated report server.
- Extend the Jenkins workflow with automated deployment and scheduled monitoring.

## 18. Conclusion

This project demonstrates a basic DevOps workflow for a Python application. GitHub provides version control, Jenkins automates testing and pipeline execution, Docker packages the application, Pytest validates application behavior, and Evidently AI generates a data drift report. Together, these components demonstrate the fundamentals of Continuous Integration, containerization, automated testing, and data monitoring.

## 19. Repository

GitHub: https://github.com/Atharv-1905/student-marks-demo
