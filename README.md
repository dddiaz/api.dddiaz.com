# Daniel Diaz's Personal Website
## Using AWS Codestar to Continously Deploy a Python API and static front end.

#### Check The Tech
- Python
- Microservices
- CI/CD
- AWS
    - Code Pipeline
    - Code Build
    - Cloud Formation
    - API Gateway 
    - Lambda
- GO Hugo (GOLANG static site generator) for front end
- HTTPS ! and Cloudfront CDN

# How to run front end locally:
```bash
cd frontend
hugo server
```

# How to make changes to prod
Easy -> git commit and aws code pipeline handles the rest :)

# What happend to the old site built with docker?
It was overkill (although it was an awesome learning expierence), and expensive to run, this is virtually free considering it uses lambda endpoints which only run when invoked, and a static front end on AWS s3.

# Dev Notes:
- Region : N. Virginia
- Make sure hugo is installed
    - brew install hugo
    - navigate to frontend folder and read readme for how to create content
    - if pycharm terminal doesnt recognize commands, make sure to open with charm .
- note you may need to invalidate the cloudfron cache, thats not automated in the buildspec yet