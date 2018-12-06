+++
title = "How Blood Glucose Stats Works"

#date = 2018-04-09
date = 2018-12-01
lastmod = 2018-12-01
draft = false

tags = ["how-it-works", "Diabetes", "Python"]
summary = "A blog post describing how the real time blood glucose stats visual works."

+++

Blood Glucose Stats works by leveraging an open source project called Nightscout. Nightscout is connected to a continuous glucose monitor (Dexcom) that I wear. The continous glucose monitor (also known as a CGM) takes a measurement every 5 minutes of the glucose levels of the interstitial fluid between cells. Those values are stored on dexcom servers and scraped by the open source Nightscout project. Night scout then tores those values in mongolab. I then use the exposed by nightscout to update the Blood Glucose graphic. While I do have access to the exact number, for privacy reasons I like to simply display a range I am in.

This is the javascript for the Glucose Visual. It's pretty hacky but it gets the job done.:
```javascript
//BG Panel JS Logic
//By: Daniel Diaz 2016

$(document).ready(function(){
    setTimeout(function() {
      $('.donut').addClass('almost-empty');
    }, 500);

    $.getJSON("<API-ENDPOINT>", function(data) {
        // This function executes on success
        var bg = data[0]["sgv"]; // Number
        var trend = data[0]['trend']; // Number
        var direction = data[0]['direction']; //String, like flat
        var returnBG = function() {
            return bg;
        }
        //Once Data is loaded, attatch an inview event to the donut
        _setBGInfoText(bg,trend,direction);
        $('.donut').bind('inview', function(event, visible) {
            if (visible) {
                _adjustBGInfoDonut(returnBG());
            } else {
                _adjustBGInfoDonutToMin();
            }
        });
    });

    //Function to adjust donut
    var _adjustBGInfoDonut = function(bg){
      if (bg){ //bg is not null or empty
        if (bg < 80){
          $('.donut').attr("class","donut one-quarter-filled");
        } else if ( bg > 180){
          $('.donut').attr("class","donut three-quarter-filled");
        } else {
          //Normal
          $('.donut').attr("class","donut half-filled");
        }
      }
    }

    var _adjustBGInfoDonutToMin = function(){
        $('.donut').attr("class","donut almost-empty");
    }

    var _setBGInfoText = function(bg,trend,direction){
        $('#glucose-text').text(_generateBGText(bg,trend,direction));
    }

    var _generateBGTrendText = function(trend,direction){
        var dir = _getDirection(direction)
        if (trend){ //bg is not null or empty
            return (" is trending "
                + dir + " by " + trend + " points");
        }
    }

    var _generateBGText = function(bg,trend,direction){
        var dir = _getDirection(direction)
        var trendText = " and no current trend info.";
        var bgText = "";
        var result = "No Last Blood Glucose Reading...";
        if (trend && direction) { //bg is not null or empty
            trendText = " and is trending " + dir + " by " + trend + " points.";
        }
        if (bg){ //bg is not null or empty
          if (bg < 80){
              bgText = "Currently my blood glucose is below average";
          } else if ( bg > 180){
              bgText = "Currently my blood glucose is above average";
          } else {
            //Normal
            bgText = "Currently my blood glucose is average";
          }
        }

        if (bgText){
            return bgText + trendText;
        }

    }

    var _getDirection = function(direction){
        if (!direction) {
            return "down"
        }
        // Technically this should also include flat, but im going to exclude it because
        // it may get confusing when pairing that with a trend number of -5 for ex.
        if (direction.lastIndexOf("Down") == -1){
            return "up"
        } else {
            return "down"
        }
    }
})
```


