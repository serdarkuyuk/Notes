# Create a new repository on the command line

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/c0ldlimit/vimcolors.git
git push -u origin master

# Push an existing repository from the command line

git remote add origin https://github.com/c0ldlimit/vimcolors.git
git push -u origin master

# GitHub Actions - CI/CD Tool (Pipelines)

Performs to automate developer workflows

what are those workflows? \

users issue problem, it is assigned to contrubuters, they fixed send pull request, managers merged code, then test, build, deployment process goes... version numbers etc.... \
when something happens in or to your repository, automatic actions are executed in response \
Github Events PR pull request, issue created, PR merged, other apps, contr. added, etc... \

1. listen to event
2. trigger workflow

Sort, label, assign it, reproduce, test, comment.. all can be done with seperate Action \
everything became workflow

most common workflow for your repository \
commit code -> test - build - push - deploy \
setup the pipeline is easy \
tool for developers \
it is compariable to jenkins

Example Pipelines \

NodeJs - Build docker image - push to nexus repo - deploy to DigitalOcean Server

Java app with maven - integration tes linux and windows - build docker image - push to AWS repo - deploy to AWS EKS

(install java, maven, docker, configure integration and plugin AWS, nexus etc...) vs git actions \
give an environment with node and docker available, with version I specify, with simply connect to target and deploy \

after pushing the github, go to actions and there are bunch of templete in groups. \
actions like setup-java, download-artifact, upload-artifact, cache, checkout are exist in github actions tab...

```yaml
name : WriteName (optional)

on: (required)
  push: (name of the github event that triggers the workflow)
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs: (when events on, below jobs executed )
  build: (arbitrary names that groups and set of actions )

   runs-on: ubuntu-latest

   steps: (required, can run commands, setup tasks or run an action)
   - uses: actions/checkout@v2 (checkout the repository, everybody checkouts )
   - name: Set up JDK 1.8
     uses: actions/setup-java@v1 (selects an action, java installed with the version 1.8)
     with:
       java-version: 1.8

   - name: Grant execute permission for gradlew
     run: chmod +x gradlew (runs a command-line command)

   - name: Build with Gradle
     run: ./gradlew build
```

when you push your request, everything in above yaml file executed in GitHub servers, but we can host in our own \
each job in a workflow runs in a fresh virtual environment \
jobs runs in parallel by default

```yaml
name : WriteName (optional)

on: (required)
  push: (name of the github event that triggers the workflow)
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs: (when events on, below jobs executed )
  build: (arbitrary names that groups and set of actions )

   runs-on: ${{matrix.os}}
   strategy:
     matrix:
       os: [ ubuntu-latex, windows-latest, macOS-latest]

   steps: (required, can run commands, setup tasks or run an action)
   - uses: actions/checkout@v2 (checkout the repository, everybody checkouts )
   - name: Set up JDK 1.8
     uses: actions/setup-java@v1 (selects an action, java installed with the version 1.8)
     with:
       java-version: 1.8

   - name: Grant execute permission for gradlew
     run: chmod +x gradlew (runs a command-line command)

   - name: Build with Gradle
     run: ./gradlew build

  publish:

    needs: build
```

go to docker hub and create an account with private repository to build everything in github actions

```yaml
  - name: build and Push Docker Image
    run: |
      docker login creditionalsi
      docker build ... tag etc...

  - name: build and Push Docker Image
    run: |
      docker login creditionalsi
      docker build ... tag etc...
    (note go to docker action market place...)
    uses: mr-smither-excellent/docker-build-push@v4
    with:
      imate: nanajanashia /demo-app
      registry: docker.io
      username: ${{ secrets.DOCKER_USERNAME }}
      password: ${{ secrets.DOCKER_PASSWORD }}
```

go to github my-project settigns, secrets and add username password \
when yaml file is ready, we copy and paste it in github my-projects/.github/workflows/ci.yaml \
when commit changes everything will be download to server
