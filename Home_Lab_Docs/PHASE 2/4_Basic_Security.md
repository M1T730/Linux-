# Setting SSH Public connection only and non-root, Basic firewalls rules with ufw, and Fail2Ban to protect against brute force attacks

**step 1:**
Set up *phase 1: 3_SSH_Connection_Key-ONLY.md* on both nodes, plus removed root login, and created a user "matteo" on both, to ssh into them.

**step 2:** (need to write it later in a firewall rules file)
Set up basic firewalls rules with UFW, in both nodes, by defaul deny all incoming traffic, and allow all outgoing traffic.
in specific:
on both nodes: allow incoming traffic from tcp 22(shh) and 8006 (proxmox GUI).
on node 1: allow forwarding traffic all (for my VM with docker inside)

**step 3:**
Set up Fail2Ban to protect both nodes against brute force attacks, followed the documentation on https://pve.proxmox.com/wiki/Fail2ban
summary: 
install Fail2Ban, set up base config, set up proxmox jail rule, set up filter job for proxmox, enable Fail2Ban.

**result** 
I've done the basic security for my home lab, need improvement, it will be done later
*reminder*: create a security file to write every rule you've implemented, to keep track of your own security choises