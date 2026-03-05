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

