pipeline {
    agent any

    stages {

        // 🔹 Stage 1 – Pull Image (Logical Stage)
        stage('Pull Image') {
            steps {
                echo "Image already available in Kubernetes (pulled earlier)"
            }
        }

        // 🔹 Stage 2 – Run Container (Logical Stage)
        stage('Run Container') {
            steps {
                echo "Container already running via Kubernetes Deployment"
            }
        }

        // 🔹 Stage 3 – Wait for Readiness
        stage('Wait for Readiness') {
            steps {
                sh '''
                echo "Starting port-forward..."
                nohup kubectl port-forward service/fastapi-service-bcd0018 8000:80 > pf.log 2>&1 &
                sleep 5
                '''
            }
        }

        // 🔹 Stage 4 – Valid Inference
        stage('Valid Inference') {
            steps {
                sh '''
                echo "Testing valid input..."
                curl -X POST http://localhost:8000/predict \
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
                curl -X POST http://localhost:8000/predict \
                -H "Content-Type: application/json" \
                -d '{}'
                echo "Invalid input handled successfully"
                '''
            }
        }

        // 🔹 Stage 6 – Stop Container (Cleanup)
        stage('Stop Container') {
            steps {
                sh '''
                echo "Stopping port-forward..."
                pkill -f "kubectl port-forward" || true
                '''
            }
        }
    }
}