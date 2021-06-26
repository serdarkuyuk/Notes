https://www.youtube.com/watch?v=7KCS70sCoK0&list=PLy7NrYWoggjw_LIiDK1LXdNN82uYuuuiC&index=6

Jenkins file is a script for pipeline

```text
pipeline {

    agent any

    stages {

        stage("build") {

            steps {

            }
        }
    }
}
```

Jenkins can be scripted or Declerative

## Scripted

first syntax \
groovy engine

node {
// groovy script
}

advanced scripting capabilities, high flexibility \
difficult to start

## Declerative

recent addition \
easier to get started but not that powerful \
pre-defined structure like this

```text
pipeline {

    agent any

    stages {

        stage("build") {

            steps {

            }
        }
    }
}
```

---

pipeline must be top-level \
agent is where to execute

pipeline {

    agent any

above part is the same as

node {

}

stages where the work happens \
stage and steps

```text
pipeline {

    agent any

    stages {

        stage("checkout") {
                configuration file...
            steps {

            }
        }

        stage("build") {

            steps {
                sh 'npm install'
                sh 'npm install'
                echo 'building the applicaiton'
            }
        }

        stage("test") {

            steps {
                // test scripts
                echo 'testing the applicaiton'
            }
        }

        stage("deploy") {

            steps {

            }
        }
    }
}
```

### Post attribute in Jenkinsfile
