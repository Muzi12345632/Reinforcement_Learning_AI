pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                //
              echo 'Build'
              sh 'virtualenv venv && . venv/bin/activate'
              //sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') { 
            steps {
                // 
              echo 'Test'
              sh 'python --version'
            }
        }
        stage('Deploy') { 
            steps {
                // 
              echo 'Deploy'
            }
        }
    }
}
