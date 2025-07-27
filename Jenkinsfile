pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yatindrap6/flask-devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('flask-devops-app')
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 flask-devops-app'
                }
            }
        }
    }
}

