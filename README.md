![CI/CD](https://github.com/dddiaz/api.dddiaz.com/workflows/CI/CD/badge.svg)

# Daniel Diaz's Personal Website API

[https://api.dddiaz.com/birthday](https://api.dddiaz.com/birthday)
[https://api.dddiaz.com/hello](https://api.dddiaz.com/birthday)

# What is this?
This is a fun little home for lambda apis hosted through my website. Above you will see a link to a sample api that
informs the user of some critical information regarding if it is my birthday or not ;)

# Dev Note:
Make sure you are using https not http when talking to api.dddiaz.com
Also for some reason, my macs default dns was not allowing this request to go thorugh, if you have issues with that, just use googles 8.8.8.8 DNS.

## TODO:
- create seperate actions for ci and cd
- run tests during ci action
- different s3 bucket for deployment
- pair down deployment permissions (in progress)
- need to figure out way to dynamically update api gateway domain mapping on each deployment
- add smoke test
- add github action for checkov for iaas scanning
