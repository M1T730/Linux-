# Setting up DNS on AD

**prereq**
have an AD DC \
install DNS service on AD 


**step 1:**
create a primary dns zone (lab.internal)\
set up A record in fowarding dns look up\
in particular for : node1, node 2, node 3, backup, ml\
ecc.... and associate with their corrispective IPs

**step 2:**\
create 2 primary reverse dns zone (192.168.10.x and 192.168.20.x)\
set up PTR record in reverse dns lookup for node1, node 2, node 3 ecc... 

Set all the hosts to use AD for DNS

LAST EDIT : 2/08/2026 