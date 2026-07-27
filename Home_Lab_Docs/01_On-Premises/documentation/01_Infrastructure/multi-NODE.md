# Making the home-lab with 2 nodes 

**step 1:**
install proxmox on a second laptop

**step 2:**
create a proxmox server, by creating a cluster, and inviting the second node to the cluster

**result:**
second node for now, has a tailscale lxc and a windows vm

**future**
use 3 nodes for the home-lab, 2 for compute, and 1 for storage, backup, high availability, and monitoring/logging ( for now, backup is implemented with a VM in node 2)