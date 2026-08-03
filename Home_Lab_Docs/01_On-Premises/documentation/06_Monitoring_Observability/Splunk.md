# Splunk configuration, installation of Splunk Universal Forwarder and created a dashboard


**step 1:** 
added it in the docker compose file in the monitoring VM, very straighfoward, just take the image and set open ports and data volume ecc...
different from others: had to accept licences and terms and set password before deploying it

**step 2:**
As Usual, installed Universal Forwarder on all nodes, made a user dedicated for it, created a service for that.

**step 3:** 
created output file to send logs to splunk server. 
created input file to take logs from journal.

**description:**
process very similar to installing promtail or node exporter for loki and prometheus rispectively, encouter some problems like indexing and parsing but resolved relatively quicky.
wrote an ansible script ( with the help of claude) to automate it on 6 nodes.
Splunk was made with the purpose of being more familiar with it and learn it progressively, thus the decision, was to deploy it identical as Loki for grafana, so seeing and (plus indexing) all logs from joirnal, it is redundant since I already had Loki, but it is made on purpose to make it more easy to learn. 

**plus:** 
* made a dashboard using claude.
* there was an app for the phone: Splunk mobile; could be enabled with a secure gateway, cool! (can use it withough vpn always on, very convinient)

DECOMMISIONED; IT WAS REDUNDANT TO LOKI, it was deployed to learn it better but will be postponed indefinitely