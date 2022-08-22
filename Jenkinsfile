pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                //
              echo 'Build'
              sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') { 
            steps {
                // 
              echo 'Test'
              // python -version
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
