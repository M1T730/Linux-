# ADDING AD TO PROXMOX's REALM, making possible for proxmox gui, using the ad to authenticate users/groups, centralized authentication

**Objective:**\
Centralized Authentication Via AD 

**Prerequisites:**\
have an AD DC, install AD CA(Certificicate Authority), create a certificate for AD 

**Architecture:**\
Right now I have 2 DCs, both can be used to Sync users using LDAP and to authenticate via Kerberos 

**Procedure:**\
activate real sync, all AD DC users and groups will be brought to Proxmox datacenter (withough permissions.), authentication only for now. 
job is set to activate every day at 21:00
actually give Proxmox's permissions to groups/users of AD's users/groups 

**Missing:**\
Having VMs and Containers (Linux based) to join the Domain and centralized their identity as well.
pfsense and applications as well

Last Edited:1/10/2026