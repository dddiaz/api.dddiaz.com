![CI/CD](https://github.com/dddiaz/api.dddiaz.com/workflows/CI/CD/badge.svg)

# Daniel Diaz's Personal Website API

[https://api.dddiaz.com/birthday](https://api.dddiaz.com/birthday)

Make sure you are using https not http when talking to api.dddiaz.com
Also for the life of me, I cant figure out why the above url does not work on my mac, but does work on other devices. My hunch is that its DNS, but still need to investigate.

## TODO:
- create seperate actions for ci and cd
- run tests during ci action
- custom api name not working
- different s3 bucket for deployment
- pair down deployment permissions
- add badge
- need to figure out way to dynamically update api gateway domain mapping on each deployment
- add smoke test