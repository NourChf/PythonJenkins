pipeline {
  agent any
  environment {
        PATH = "/path/to/python/bin:${env.PATH}"
    }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
