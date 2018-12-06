+++
title = "re:invent 2018"

date = 2018-12-05
lastmod = 2018-12-05
draft = false

tags = ["AWS", "DEVOPS", "Cloud Migration", "Fintech"]
summary = "Major Take Aways From re:Invent"

[header]
image = "headers/reinvent2018.jpeg"

+++

This year I was fortunate enough to go to re:Invent, the AWS Tech Conference. 
I wanted to use this opportunity to document some of my major take aways.

# Full Stack Ownership
Infrastructure (as well as test code) code lives with microservice code in the same Bitbucket project (potentially different repos within that project)

# "Everything As Code"
Including policy, security, and infra.
    
# Vanguard Cloud Journey: 
I highly reccoment listening to this podcast I listened to on my flight home:  
    https://itunes.apple.com/us/podcast/on-cloud/id1406374662?mt=2&i=1000424769753 (listen to podcast released on: 11/28/2018)  
__Cloud is not a destination, it's an enabler (of cd and innovation)__  
Vanguard initially had a goal of multi cloud deployments, but decided it wasn't technically feasible.  
     May be better to only consider a different cloud offering only when they offer a specific capability.  
Initially had lift and shift approach, but pivoted away to just refactor, and make cloud native.  
    I see this as a common occurance to, which is unfortunate because it misses out on all the innovatin the cloud delivers.  
# 2 pizza teams
Led by business owners, devs get assimilated into business units eventually  
# CICD for INFRA
CFN-LInt, CFN-TAG, and taskcat for cloudformation to enable cicd for infrastructure.  
# At dev layer, don't restrict
Allow devs to experiment (within AWS as well)  
Open network, open machine   
This probably seems obvious in non regulated companies, but this is something I have seen regulated companies strugle with.  


