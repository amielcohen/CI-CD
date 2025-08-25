pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo '🔨 Build stage starting'
        sh '''
          echo "Doing the build..."
          # שים כאן את פקודות הבילד האמיתיות שלך, למשל:
          # npm ci && npm run build
          # mvn -B -DskipTests package
          # pip install -r requirements.txt
        '''
      }
    }
  }
  post {
    always { echo "Build result: ${currentBuild.currentResult}" }
  }
}
