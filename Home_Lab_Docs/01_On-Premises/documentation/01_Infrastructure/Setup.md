# Setting up Proxmox

Installation of Proxmox using an USB flash drive (used BalenaEtcher), Currently running Proxmox 9.2.6.

All the nodes joined a DataCenter, Corosync manages the cluster, 3 nodes was a deliberate choise, if 1 node goes down I still have the majority, 2, nodes up for quorum.

Currently have 3 nodes: 
pve       192.168.20.2
node 1    192.168.20.3
node 2    192.168.20.4

All VMs are running with KVM technology and container are running either with Docker or LXC. 

ISO images used: 
Ubuntu 24.04.0 server
netgate 1.1.1
proxmox backup 4.2.4
Win11 x64
windows server core 2025




LAST EDIT : 2/08/2026