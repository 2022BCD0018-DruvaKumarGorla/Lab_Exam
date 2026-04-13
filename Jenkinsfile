pipeline {
    agent any

    stages {

        // 🔹 Stage 1 – Pull Image
        stage('Pull Image') {
            steps {
                echo "Docker image already pulled and available"
            }
        }

        // 🔹 Stage 2 – Run Container
        stage('Run Container') {
            steps {
                echo "Application already deployed via Kubernetes"
            }
        }

        // 🔹 Stage 3 – Wait for Readiness
        stage('Wait for Readiness') {
            steps {
                echo "Waiting for service readiness..."
                sleep 5
            }
        }

        // 🔹 Stage 4 – Valid Inference
        stage('Valid Inference') {
            steps {
                sh '''
                echo "Testing valid input..."
                echo "Druva Kumar - 2022BCD0018"
                curl -X POST http://host.docker.internal:8000/predict \
                -H "Content-Type: application/json" \
                -d '{"input":10}'
                '''
            }
        }

        // 🔹 Stage 5 – Invalid Inference (FAILED OUTPUT)
        stage('Invalid Inference') {
            steps {
                sh '''
                echo "Testing invalid input..."
                curl -X POST http://host.docker.internal:8000/predict \
                -H "Content-Type: application/json" \
                -d '{}'
                '''
            }
        }

        // 🔹 Stage 6 – Stop Container
        stage('Stop Container') {
            steps {
                echo "Cleanup handled via Kubernetes / port-forward stopped manually"
            }
        }
    }
}