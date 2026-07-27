# Changing IPs

# Proxmox hosts: 

**step 1:**
*change the ip of the node:*
modify the interface, in particular vmbro0.20, and change the ip to the desired one, apply configuration and go to new_ip:8006 for the new gui. 
remember to change /etc/hosts as well
**step 2:**
*sync the change to the other nodes* 
modify on each node the /etc/corosync/corosync.config file, and change the ip address of the node, dont forget to add +1 to the version of the file. 
then restart the corosync.service on each node.


# VMs/LXCs

**step 1**:
this is pretty straight foward, I will take it for granted that it is to change an static dhcp addr. so just change the ip there and clear the arp table. 



# AFTER
for both then do: 

* change the ip that prometheus config file uses to take the metrics
* change the ip that I use for ansible hosts.ini file and zsh.rc file as well
