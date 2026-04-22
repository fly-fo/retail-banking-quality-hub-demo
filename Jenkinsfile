pipeline {
    agent {
        label 'python'
    }

    parameters {
        string(name: 'BROWSER', defaultValue: 'Chrome', description: '')
        string(name: 'OS', defaultValue: 'Linux', description: '')
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
                    python3 --version
                    python3 -m pip --version || python3 -m ensurepip --upgrade || true
                    python3 -m pip install --upgrade pip --user || true
                    python3 -m pip install -r requirements.txt --user || python3 -m pip install -r requirements.txt --break-system-packages --user
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
                        export PATH="$HOME/.local/bin:$PATH"
                        python3 -m pytest tests/api tests/e2e tests/manual --alluredir=allure-results
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