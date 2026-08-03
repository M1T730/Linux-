# Setting Proxmox Backup Server 

**step 1:**
Download and set up Proxmox backup server.(temporaly on a vm inside node 2,later on I will set up a node 3)

**step 2:**
Create Datastore and setup right permissions, add PBS storage into the main Datacenter Proxmox

**step 3:**
Create backup jobs and enable pruning:
backup jobs: daily at 3:00 for ID: 100,101,102,105,200,300,600
Pruning: daily at 00:00 (before backup to keep snapshots as long as possible within the day) 
Last:7, Day: 7, Week: 4, Mounth: 3 (not much because I don't have a lot of storage)
Garbege collection EveryDay at 5:00 (ensure backups is done)
verify jobs weekly. 

LAST EDIT : 3/08/2026