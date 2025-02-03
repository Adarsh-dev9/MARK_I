pipeline {
    agent any

    environment {
        TOMCAT_USER = 'robot'
        TOMCAT_PASSWORD = 'robot'
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
         stage('Verify WAR File') {
                    steps {
                        script {
                            def warExists = fileExists('target/mark-1-webapp-adarsh-1.0.0-SNAPSHOT.war')
                            if (!warExists) {
                                error("❌ WAR file not found! Build failed.")
                            }
                            else{
                                echo "War file exists"
                            }

                        }
                    }
                }
        stage('Deploy to Tomcat') {
            steps {
                sh '''
                curl -v --upload-file target/mark-1-webapp-adarsh-1.0.0-SNAPSHOT.war \
                     --user "robot:robot" "http://localhost:8081/manager/text/deploy?path=/mark-1-webapp-adarsh-1.0.0-SNAPSHOT&update=true"
                     '''
            }
        }
    }
}