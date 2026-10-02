# Setting up DNS

**prereq**
have an AD DC \
install DNS service on AD 

**Objective:**\
Setting DNS on AD DCs for Hosts in the Cluster and VPN clients

**Architecture:**\
Having 2 DNS services on both AD DCs, DC01 being the primary and DC02 being the backup, falling back to the ISP's router for anyother

**Procedure:**\
create a primary dns zone (lab.internal)\
set up A record in fowarding dns look up\
in particular for : node1, node 2, node 3, backup, ml\
ecc.... and associate with their corrispective IPs
create 2 primary reverse dns zone (192.168.10.x and 192.168.20.x)\
set up PTR record in reverse dns lookup for node1, node 2, node 3 ecc... 
Set all the hosts to use AD DCs for DNS

**Troubleshooting:**\
traffic flow: local cache --> DC01 if not UP DC02 ---> ISP --> ..... --> Authoritative server  

LAST EDIT : 1/10/2026 