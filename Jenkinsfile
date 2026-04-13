pipeline {
    agent any

    environment {
        IMAGE_NAME = "druva21/fastapi-app-bcd0018"
    }

    stages {

        stage('Pull Image') {
            steps {
                sh 'docker pull $IMAGE_NAME'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 $IMAGE_NAME'
            }
        }

        stage('Wait for Readiness') {
            steps {
                sleep 10
            }
        }

        stage('Valid Inference') {
            steps {
                sh '''
                curl -X POST http://localhost:8000/predict \
                -H "Content-Type: application/json" \
                -d '{"input":10}'
                '''
            }
        }

        stage('Invalid Inference') {
            steps {
                sh '''
                curl -X POST http://localhost:8000/predict \
                -H "Content-Type: application/json" \
                -d '{}'
                '''
            }
        }

        stage('Stop Container') {
            steps {
                sh 'docker stop $(docker ps -q)'
            }
        }
    }
}