pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Login to ECR') {
      steps {
        script {
          if (env.AWS_CREDENTIALS_ID?.trim()) {
            withCredentials([[$class:'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
              sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
            }
          } else {
            sh "aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
          }
        }

      }
    }

    stage('Build image') {
      steps {
        sh '''
          GIT_SHA=$(git rev-parse --short HEAD)
          docker build -t \'"${IMAGE}"\':$GIT_SHA -t \'"${IMAGE}"\':latest .
        '''
      }
    }

    stage('Push to ECR') {
      steps {
        sh '''
          GIT_SHA=$(git rev-parse --short HEAD)
          docker push \'"${IMAGE}"\':$GIT_SHA
          docker push \'"${IMAGE}"\':latest
        '''
      }
    }

    stage('Deploy to EC2') {
      steps {
        sshagent(credentials: [env.SSH_CRED_ID]) {
          sh '''
            GIT_SHA=$(git rev-parse --short HEAD)
            ssh -o StrictHostKeyChecking=no \'"${PROD_HOST}"\' \'
              set -e
              aws ecr get-login-password --region \'"${AWS_REGION}"\' | docker login --username AWS --password-stdin \'"${ECR_REGISTRY}"\'
              docker pull \'"${IMAGE}"\':$GIT_SHA || docker pull \'"${IMAGE}"\':latest
              docker rm -f flaskapp || true
              docker run -d --name flaskapp --restart unless-stopped -p \'"${RUN_PORT}"\':\'"${APP_PORT}"\' \'"${IMAGE}"\':$GIT_SHA ||               docker run -d --name flaskapp --restart unless-stopped -p \'"${RUN_PORT}"\':\'"${APP_PORT}"\' \'"${IMAGE}"\':latest
            \'
          '''
        }

      }
    }

  }
  environment {
    AWS_REGION = 'us-east-1'
    ECR_REGISTRY = '992382545251.dkr.ecr.us-east-1.amazonaws.com'
    ECR_REPOSITORY = 'amiel'
    IMAGE = "${ECR_REGISTRY}/${ECR_REPOSITORY}"
    APP_PORT = '5000'
    RUN_PORT = '80'
    AWS_CREDENTIALS_ID = 'aws-creds'
    PROD_HOST = 'ec2-user@<PROD_EC2_PUBLIC_IP>'
    SSH_CRED_ID = 'prod-ssh'
  }
  post {
    always {
      sh 'docker image prune -f || true'
    }

  }
  options {
    timestamps()
  }
}