# Setting up Ubuntu Server (Proxmox now)

**Using an USB**

**step 1:**
installing Ubuntu 24.04.4 LTS ISO image from https://ubuntu.com/download/server#manual-install-tab

**step 2:**
Create a bootable USB flash drive using BalenaEtcher

**step 3:**
Boot from the USB flash drive, from the boot menu and setting up the the initial configuration

**step 4:** (painfull process)
Once finished, Manually setup Wi-fi Connection, laptop didn't have ethernet port, editing */etc/netplan*

**update_afterstep5**
now using ethernet because proxmox would ve been difficult with WI-FI