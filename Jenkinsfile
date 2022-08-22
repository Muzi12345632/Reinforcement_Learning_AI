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
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                // 
              echo 'Test'
              sh 'python --version'
              sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
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
