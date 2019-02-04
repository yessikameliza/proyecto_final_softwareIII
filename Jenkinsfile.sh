#!/usr/bin/env bash
pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/main.py sources/Persistence.py'
            }
        }
    }
}