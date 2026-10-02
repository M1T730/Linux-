**Automated Deployment Script for Windows in HyperV**
there are 2 main processes: creation + configuration; there are many ways to implement this: 
* just use Intune
* template + GPOs, PXE + GPOs ecc...
* Powershell + Ansible/ Windows unattended setup  + GPOs
* windows native solutions + GPOs 
and many more...

I choose to use Powershell with the HyperV module to create the VM from a Golden Image, Powershell Direct to  automatically join the Windows VM to the domain then GPO will do the rest of the configuration. I choose this because it let me practice with Poweshell + GPOs, I could use ansible instead of Powershell Direct or GPOs but I dont really need to force it everywhere. 
The other solutions were discarded based on what I want and need to learn and no other criterias were involved. (to be honest i'm very interest in Intune But I will postpone it Until I make a Hybrid Entra + AD infra for SSO).


**Install vaeem community edition** (remember 10 vms limit), and use it for vms, keeping pbs for lxcs for proxmox, using vaeem for the soleny advantage of cross-hypervisor backups.
My objective is to have a proxmox cluster and a hyperV node running ad dc and windows workstations + veaam itself in it(node4)

pros: cross-hypervisor backup/replicication and because its the leading on-premises solution for backups, so good practice for real world cases

cons: having 2 backups server: veaam and pbs, not fully native to proxmox (where most of my workload is) and added operational complexity


**Migrate  AD DC and windows workloads to the new node 4** running HyperV, using Veeam and its cross-hyperviror fuctionality, instead of backing the vm into tar then convert it into .vhd/.vhdx

compared to a manual migration

pros: operational simplicity after migration, cross-hypervisor backsups and replication

cons: migration itself, need for a third party solution, non proxmox native. 


**Kasm** for VDI, this to practice Citrix logix withough spending money for Citrix licence; install kasm agents to windows workloads to make them as VDI, and use kasm unique feature of Streaming Containers, so for desktops use Windows VMs and for applications use kasm unique feature. 

compared to citrix: 

pros: free version of VDI, has very similar characteristic: login/ad integration/VDIs/agets, Similar VDI logic although different, can use containers as well, partner of Proxmox, can use natevely Proxmox APIs for automatic life cycles.

cons: uses rdp instead of citrix protocol, lacking in windows integration, similar but not equal to citrix, used on the browser instead of an application



others: implement fully AD for applications, identity and user permissions; better log and metric life management; rethink the use of resouces: cpu/storage and ram. implement cloud backups(free if possible) and automatic synchronication; Automatic generation of a Report(weekly), modify the ips of PBS and PDM back to subnet 192.168.10.x and its correspective firewall rules, dns ecc...

**MAYBE**:

**Create a management VM:**
Fully give this VM permissions to manage all the infrastructure + Use this VM for everything related to HyperV instead of using my macbook M1, my objective is to be able to connect any device to my vpu but only those that can access the management VM can modify the actual infrastrucure.

pros: centralized management, less attack surface

cons: single point of failure, need vpn to be always on, if I blocked myself out of VPN It will be very annoying, the vm needs to be resilient. 

requirement: Multiple of these, Redundant Network applications + VPN and always a way to manage vms locally.
I will probably just run a management VM for hyperV only temporaly and once the infrastructure is resiliant enough I will consider to fully untrust my personal device to only use Management VMs/Machines.

LAST EDIT : 1/10/2026