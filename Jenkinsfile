// --- tiny helper functions (pure Groovy, no Jenkins steps here) ---
def banner(String msg) { return "\n===== ${msg} =====" }
def mkVersion(String branch, String buildNum) {
  return ((branch ?: 'local') + "-" + (buildNum ?: '0')).toLowerCase()
}
def fakeHash(int len = 8) {
  def chars = (('a'..'f') + ('0'..'9')).join()
  def r = new Random()
  (1..len).collect { chars[r.nextInt(chars.length())] }.join()
}

pipeline {
  agent any

  options { timestamps() }

  parameters {
    booleanParam(name: 'SLOW_MODE', defaultValue: false, description: 'Add small sleeps to simulate work')
    string(name: 'ENV', defaultValue: 'dev', description: 'Target environment (fake)')
  }

  environment {
    APP_NAME = 'demo-app'
  }

  stages {
    stage('Info') {
      steps {
        script {
          echo banner('Pipeline Info')
          echo "Job: ${env.JOB_NAME} | Branch: ${env.BRANCH_NAME} | Build: #${env.BUILD_NUMBER}"
          echo "Env param: ${params.ENV}"
          if (params.SLOW_MODE) sleep time: 1, unit: 'SECONDS'
        }
      }
    }

    stage('Prepare') {
      steps {
        script {
          echo banner('Prepare workspace')
          sh 'mkdir -p build && echo "nothing to see here" > build/.keep'
          if (params.SLOW_MODE) sleep time: 1, unit: 'SECONDS'
        }
      }
    }

    stage('Build') {
      steps {
        script {
          echo banner('Fake Build')
          def ver  = mkVersion(env.BRANCH_NAME, env.BUILD_NUMBER)
          def hash = fakeHash(10)
          writeFile file: 'build/build.txt', text: """\
            app=${env.APP_NAME}
            version=${ver}
            fake_commit=${hash}
            target_env=${params.ENV}
          """.stripIndent()
          echo "Produced fake artifact metadata: version=${ver}, hash=${hash}"
          if (params.SLOW_MODE) sleep time: 2, unit: 'SECONDS'
        }
      }
    }

    stage('Quality Gates') {
      parallel {
        stage('Lint') {
          steps {
            script {
              echo banner('Lint (fake)')
              sh 'echo "lint ok" > build/lint.txt'
              if (params.SLOW_MODE) sleep time: 1, unit: 'SECONDS'
            }
          }
        }
        stage('Unit Tests') {
          steps {
            script {
              echo banner('Unit Tests (fake)')
              sh 'echo "tests ok" > build/tests.txt'
              if (params.SLOW_MODE) sleep time: 1, unit: 'SECONDS'
            }
          }
        }
      }
    }

    stage('Package') {
      steps {
        script {
          echo banner('Package (fake)')
          // No real packaging; just touch a pretend artifact
          writeFile file: 'build/artifact.txt', text: 'pretend binary bytes'
          archiveArtifacts artifacts: 'build/**', fingerprint: true
          if (params.SLOW_MODE) sleep time: 1, unit: 'SECONDS'
        }
      }
    }

    stage('Deploy (fake)') {
      steps {
        script {
