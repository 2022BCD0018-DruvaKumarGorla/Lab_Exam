pipeline {
    agent any

    stages {

        stage('Pull Image') {
            steps {
                echo 'Image already pulled manually'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Container already running via Kubernetes'
            }
        }

        stage('Wait for Readiness') {
            steps {
                sleep 5
            }
        }

        stage('Valid Inference') {
            steps {
                sh '''
                curl -X POST http://host.docker.internal:30007/predict \
                -H "Content-Type: application/json" \
                -d '{"input":10}'
                '''
            }
        }

        stage('Invalid Inference') {
            steps {
                sh '''
                curl -X POST http://host.docker.internal:30007/predict \
                -H "Content-Type: application/json" \
                -d '{}'
                '''
            }
        }

        stage('Stop Container') {
            steps {
                echo 'Handled by Kubernetes'
            }
        }
    }
}