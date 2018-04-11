+++
title = "How Blood Glucose Stats Works"

date = 2018-04-09
lastmod = 2018-04-09
draft = false

tags = ["how-it-works", "Diabetes", "Python"]
summary = "A blog post describing how the real time blood glucose stats visual works"

[header]
image = "bg.png"

+++

Blood Glucose Stats works by leveraging an open source project called Nightscout. Nightscout is connected to a continuous glucose monitor that I wear on my body to get current glucose values. Those values are stored in mongolab, and I use the api on dddiaz.com to query that database to update the glucose graphic in real time.


