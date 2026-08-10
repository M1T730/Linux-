# Implementing NGINX

**Objective:** 
Improve security by opening only port 80 ( in future 443) for applications instead of 4533, 8123 ....\
Learn how to use a reverse proxy, in particular, for my specific need to write only http://navidrome.lab.internal in the browser instead of http://192.168.10.3:4533 or http://navidrome.lab.internal:4533 to listen to music with navidrome. 

**Process:**
Created an Nginx container in the Docker VM (contains the applications)\
created a docker network and and made all the applications + ngxing to use it.\
written the nging config file to send the traffic to the correct application based on the url.

IN PARTICULAR: 

home_assistant.lab.internal   to   http://home_assistant:8123
navidrome.lab.internal        to   http://navidrome:4533 
uptimekuma.lab.internal       to   http://uptimekuma:3001
jellyfin.lab.internal         to   http://jellyfin:3001