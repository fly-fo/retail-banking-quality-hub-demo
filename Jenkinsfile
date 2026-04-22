pipeline {
    agent any

    environment {
        ALLURE_ENDPOINT = 'https://demo.testops.cloud'
        ALLURE_PROJECT_ID = '4601'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_LAUNCH_NAME = 'retail-banking-quality-hub-demo-jenkins'
        ALLURE_TOKEN = credentials('ALLURE_TOKEN')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version || python --version
                    python3 -m venv .venv || python -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install allurectl') {
            steps {
                sh '''
                    curl -fsSL https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_amd64 -o allurectl
                    chmod +x allurectl
                '''
            }
        }

        stage('Run API + E2E + Manual') {
            steps {
                sh '''
                    . .venv/bin/activate
                    ./allurectl watch -- pytest tests/api tests/e2e tests/manual --alluredir="$ALLURE_RESULTS"
                '''
            }
        }
    }
}