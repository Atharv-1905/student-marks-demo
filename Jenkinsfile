pipeline {
    agent any

    environment {
        IMAGE_NAME = "student-marks-demo"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Pull Code from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Docker Application Test') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Docker Pytest') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                sh '''
                    mkdir -p monitoring/reports
                    docker run --rm \
                      -v "$WORKSPACE/monitoring/reports:/app/monitoring/reports" \
                      ${IMAGE_NAME}:${IMAGE_TAG} \
                      python monitoring/data_drift.py
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'monitoring/reports/drift_report.html', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All CI stages completed!'
            echo 'Jenkins pipeline execution finished.'
        }
    }
}
