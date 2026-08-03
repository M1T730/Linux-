# ADDING AD TO PROXMOX's REALM, making SSO possible for proxmox gui, using the ad to authenticate users/groups

adding ad to proxmox's REALM permits me to authenticate to the Proxmox GUI with an AD user, centralizing User management (will add it to containers as well)

**prereq:** 
have an AD DC, install AD CA, certificate AD DC. 

**step 1:**
make so that Proxmox trusts AD CA's certificates
copy the AD CA's certificate to /usr/local/share/certificate
then do update-ca-certificate 
repeat on all nodes. 

**step 2:**
add the AD DC to proxmox realm 
binding a user as well

**step 3:**
activate real sync, all AD DC users and groups will be brought to Proxmox datacenter (withough permissions.), authentication only for now. 
job is set to activate every day at 21:00

**step 4:**
actually give Proxmox's permissions to groups/users of AD's users/groups 


LAST EDIT : 3/08/2026