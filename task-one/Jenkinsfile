pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'shaykekeidar/test-for-elisra'
        IMAGE_TAG = 'latest'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/shaykekeidar/test-for-elisra.git', branch: 'main'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    image = docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}")
                }
            }
        }
        
        stage('Login to Docker Hub and Push') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials-id') {
                        image.push()
                    }
                }
            }
        }
    }
}