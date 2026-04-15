# Tailscale (vpn)

I did this way back, but never documented it, first my setup was tailscale on each node, so node 1 and node 2, each hat their tailscale container, each that could let me manage remotely my machines in those respectively nodes;
I've centralized mysetup after setting up PFSense. 

**prereq:**
have pfsense server
have a tailscale account 
**step 1:**
Generate a auth key in tailscale account, setting up tailscale on pfsense, so installing package and putting the auth key

**step 2:**
configure the subnets you want to have remote access to, for example: 192.168.20.0/24 and 192.168.10.0/24. 

**result:** 
now I can access my home network from outside by just having wifi and a device with my tailscale account connected, the difference between my decentralized setup and centralized setu is really just come down to the fact that management and future operations(dns and acls) will be done on a single tailscale machine instead of multiples.