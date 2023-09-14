# audius-tools
Messing around with the audius api/sdk


This tool allows developers to visualize what is needed to stream a track from Audius.

First, you will need to select a host from api.audius.co.
  I choose a random healthy node by returning a random value from the array and storing it as my host variable. 
  
1) The track ID is required to be resolved from the original audius.co URL for the track.
2) Then you are able to hit the streaming endpoint to interact with the mp3 file.
