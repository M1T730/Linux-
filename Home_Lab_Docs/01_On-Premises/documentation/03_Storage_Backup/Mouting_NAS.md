# Mouting Nas on VM
mouting LXC's Share as if it were a physical external drive

**Prerequisites:**
having an samba server, outside VM
installing cifs utilities to allow Linux to access Samba share

```bash
sudo apt update
sudo apt install -y cifs-utils
```

**step 1:**
create a mount point: 
and create a secret file for credentials
```bash
sudo mkdir -p /mnt/nas_music
vim ~/.smbcredentials
```
inside .smbcredentials:
username=your_samba_username
password=your_samba_password

**step 2:**
modify */etc/fstab*  to automatically mount smb share at boot

```bash
sudo nano /etc/fstab
```
add:
//10.10.10.2/NAS/Musica /mnt/nas_music cifs credentials=/home/docker/.smbcredentials,iocharset=utf8,gid=1000,uid=1000 0 0

**Verification:**
```bash
sudo mount -a
ls /mnt/nas_music
systemctl daemon-reload 
```

