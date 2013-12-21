#global define 
 "use strict"
@app = window.app ? {}

require ["jquery", "moment"], ($, datetime) ->
  $ ->
    currentTime = () ->
      setInterval () ->
        $('.current-date').text(datetime().format('MMMM Do YYYY, h:mm:ss a'))
      , 1000

    currentTime() if $('.current-date')
    console.log "Po Up, drank."