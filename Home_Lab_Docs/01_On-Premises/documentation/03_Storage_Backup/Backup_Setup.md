# Setting Proxmox Backup Server 

**step 1:**
Download and set up Proxmox backup server.(temporaly on a vm inside node 2,later on I will set up a node 3)

**step 2:**
Create Datastore and setup right permissions, add PBS storage into the main Datacenter Proxmox

**step 3:**
Create backup jobs and enable pruning:
backup jobs: every day at 3:00, backing up Tailscale Lxc for both nodes, Ubuntu VM in the first node and NAS in the first node
Pruning: Last:7, Day: 7, Week: 4, Mounth: 3 (not much because I don't have a lot of storage)

**step 4:**
Set up Garbage collection and verify jobs weekly. 

