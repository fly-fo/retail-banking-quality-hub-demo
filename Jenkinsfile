pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('git pull') {
            steps {
                git branch: 'main', url: 'https://github.com/fly-fo/retail-banking-quality-hub-demo.git'
            }
        }

        stage('Setup Python env') {
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

        stage('Run tests and upload to Allure TestOps') {
            steps {
                withAllureUpload(
                    credentialsId: 'Amir-Demo.test.cloud',
                    name: "${JOB_NAME} - #${BUILD_NUMBER}",
                    projectId: '4601',
                    serverId: '4601@Demo.testops.cloud',
                    tags: 'jenkins, api, e2e, manual',
                    indexExistingFiles: true,
                    results: [[path: 'allure-results']]
                ) {
                    sh '''
                        . .venv/bin/activate
                        pytest tests/api tests/e2e tests/manual --alluredir=allure-results
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}