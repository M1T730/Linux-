# Backups 

**Objective:**\
Having a Proxmox's Native Backup server, Proxmox backup server, for LXCs within Promox and non essential VMs.\
Have Veaam Comminity ediction For Critical VMs, being able to replicate between hypervisors. 

**Architecture:**\
Proxmox Backup Server:\
Data stores connected to the Datacenter.\
backup jobs: daily at 3:00 with a 500Mbps max bandwidth\ 
Pruning: daily at 5:00 (ensure backups are done) \
Last:5, Day: 5, Week: 2, Mounth: 1 (not much because I don't have a lot of storage)\
Garbege collection EveryDay at 6:00 (ensure pruning is done)
verify jobs weekly. 

**Missing:**\
Veamm 



LAST EDIT : 1/10/2026