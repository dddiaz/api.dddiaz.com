# Frontend Website

## PreReqs:
- Hugo
    - Normally you can install with brew hugo but my site has a dep on an older version
    - You can install this using the install_hugo.sh script located in the root of the project

## How to Run
- CD to frontend
- hugo server -w to run

## How to create a post
- type hugo new post/post-name.md to create a new blog post
- Dont forget you can set a post for a future pub date

## Dev Notes
https://discourse.gohugo.io/t/solved-inject-an-svg-file-into-my-html/7446/6

Other Notes
- Note i created a custom glucose widget to support the inline theme
- Note that my cloudfront distrubition whitelists only a couple countries. So if you cant see the site, make sure you are on the whitelist.
- Go Hugo blog posts (aka sub directories) dont show up (AKA acess denied) when distributed with cloud front 
    - FIX: https://stackoverflow.com/questions/31017105/how-do-you-set-a-default-root-object-for-subdirectories-for-a-statically-hosted ?