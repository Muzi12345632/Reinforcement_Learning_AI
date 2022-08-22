pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                //
              echo 'Build'
              pip install -r requirements.txt
            }
        }
        stage('Test') { 
            steps {
                // 
              echo 'Test'
              echo python --version
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
