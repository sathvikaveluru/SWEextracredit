pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sveluru2/studentsurvey646:8.0"
    }

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git 'https://github.com/sathvikaveluru/SWEextracredit.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl set image deployment/studentsurvey studentsurvey=$DOCKER_IMAGE"
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment successful!"
        }
        failure {
            echo "❌ Build or deployment failed."
        }
    }
}
