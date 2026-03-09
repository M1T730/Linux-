# Setting NAS with SAMBA(allows inter-OS communication)

**Prerequisites:**
make a directory for nas: *mkdir -p /srv/nas*
create a group for nas: *sudo groupadd nasusers*
add your user to the group: *sudo usermod -aG nasuers $USER* 
change nas directory to group: *sudo chown -R :nasusers /srv/nas
change nas directory permissions (alows xwr for user and group): *sudo chmod 770 /srv/nas*

**step 1:**
installing samba: 
*sudo apt update*
*sudo apt install samba*

**step 2:**
configuring samba in */etc/samba/smb.conf*
[NAS]
    path = /srv/nas
    browsable = yes
    writable = yes
    guest ok = no
    read only = no
    create mask = 0660
    directory mask = 0770
very self explanatory config. 

**step 3:**
creating samba users and enabling them:
*sudo smbpasswd -a user*
*sudo smbpasswd -e user*

**step 4:**
restarting samba server:
*sudo systemctl restart smbd*
*sudo systemctl enable smbd*

**Extra:**
for Macos: open finder, press cmd+k, connect to smb://server_ip
for Linux: open filesystem, go to server, connect to smb://server_ip


**Update_afterstep5** (after installing proxmox and setting an LXC container for the NAS(SAMBA))

modify router settings, adding Static Route, 
address: 10.10.10.# (LXC's IP)
subnet:  255.255.255.0/24
gateway: 192.168.1.# (Proxmox's IP)

Router now knows that the traffic for 10.10.10.# has to be sent to Proxmox's IP
*Why you need this?* because router does not allow multiple MAC addresses on the same LAN port, so we bypass it making our Proxmox host become a router, to create a NAT