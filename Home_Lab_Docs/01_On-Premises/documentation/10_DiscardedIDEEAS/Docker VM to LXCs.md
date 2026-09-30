# Migrating Docker VM to a 4 LXCs 

**Procedure:**\
The Plan was to migrate 1 application at the time.\
Creating backups based on the Docker volumes.\
creating each LXC (apart from navidrome and jellyfin, they would've been together) installing the application with the data from the volumes.\
create an internal virtual switch for connectivity between Nginx and applications.

**Pros:**
* more isolation
* resource efficiency 
* individual service troubleshooting
* divided failure domains

**Cons:**
* less portable between hypervisors (a characteristic I value a LOT)
* more complicated 

**Judgement:**\
I considered the plan and though about how to implement this, the main reason I wanted to do this was to reduce the number of VMs, for Veeam.\
I judged that this plan will not be done, although there are benefits (listed in the pros), the cons outweight the pros.\
To implement a host virtual switch, I would've made portability none, to implement portability I would need to create a new VLAN and virtual bridged on each proxmox hosts, making it more complex, and put more strain on my physical network setup (very slow, all cables are 1Gbps).\ 
With all the variabes considered I choose to keep the simple implementation, a VM running Docker, running applications written in a docker compose file, for the sole purpose of portability.

LAST EDIT : 30/09/2026