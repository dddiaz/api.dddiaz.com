+++
title = "Docker AWS Pipeline"

date = 2018-04-09
lastmod = 2018-04-09
draft = false

tags = ["how-it-works", "CI", "CD", "AWS", "Docker", "Python"]
summary = "A blog post describing how this website was built and deployed (CI/CD AWS Docker)"


+++

The previous version of this website used docker and aws code pipeline to continuously deploy to elastic beanstalk.

Here is the buildspec.yml
```yml
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Docker Hub...
      - docker login --username="$DOCKER_HUB_USERNAME" --password="$DOCKER_HUB_PASSWORD"          
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
      - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $IMAGE_REPO_NAME:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - docker push $IMAGE_REPO_NAME:$IMAGE_TAG
```

If you are really curious the full source can be found on [github](https://github.com/dddiaz/Home)

