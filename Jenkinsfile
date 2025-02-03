pipeline {
    agent any

    environment {
        TOMCAT_USER = 'jenkins'
        TOMCAT_PASSWORD = 'jenkins123'
        TOMCAT_HOST = 'http://localhost:8081'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Adarsh-dev9/MARK_I.git'
            }
        }
        stage('Build with Maven') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Deploy to Tomcat') {
            steps {
                sh '''
                curl -v --upload-file target/mark-1-webapp-adarsh-1.0.0-SNAPSHOT.war \
                "$TOMCAT_USER:$TOMCAT_PASSWORD@$TOMCAT_HOST/manager/text/deploy?path=/mark-1-webapp-adarsh-1.0.0-SNAPSHOT&update=true"
                '''
            }
        }
    }
}