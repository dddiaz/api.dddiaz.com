+++
title = "iTerm2 Glucose"
date = 2020-02-21T18:33:16-08:00
draft = false

tags = ["iTerm", "Diabetes", "Nightscout", "Oh-My-Zsh", "We Are Not Waiting"]
summary = "How I display my current Blood Glucose in iTerm"

[header]
image = "headers/nightscout-cronjob.png"

+++

# Background
iTerm2 with oh-my-zsh is my goto environment for doing anything on the command line.
The tool allows infinite amounts of customization.
Recently they announced a feature called the status bar.
You can check out the feature [here](https://www.iterm2.com/documentation-status-bar.html).
It lets you display nifty information like current CPU/Network/Mem Utilization.
What is really cool though, is that you can take it a step further.
You can customize it to display your current kubernetes context or even your current AWS Profile.
This got me thinking, I wonder if I could display my current Blood Glucose there?

# Problem Statement
So the question is, how can I display my current blood glucose on my terminal.

# First Attempt
I am running an open source website called [Nightscout](http://www.nightscout.info/) that scraped my blood glucose data from a continuous glucose monitor that I wear on my body.
This site also exposes an endpoint I can GET to obtain my current blood glucose reading. So my first thought was, this should be simple.
All I need to do is curl that endpoint and then display that in my terminal.

#### Not so FAST!
I immediately noticed that while this solution worked, it seriously slowed down the speed of my terminal.
What was happening was that every time I executed a command, my terminal would attempt to update my current glucose by curling the endpint.
This added about half a second of latency to my terminal, that gives the immpression of an unresponsive dev tool.

# There has to be a better way...
And there is! I decided that what I could do instead is just have a cron job that runs on my mac, curls that endpoint every 3 mintues, and writes the result to a file.
Then from there, I could just output the text of that file in my terminal prompt! Now that is super fast! 

# Hey, this sounds cool, how do I get set up?
Check out the repo at [github](https://github.com/dddiaz/nightscout-cronjob).
There you will find all the instructions you need to get setup.
Happy Hacking



