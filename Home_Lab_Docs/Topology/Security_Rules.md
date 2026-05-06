# UFW:

# THESE RULE ARE NOT UPDATED NOR ACTIVE RIGHT NOW; I NEED TO REWRITE THIS

**Node 1:**
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere             # ssh        
8006/tcp                   ALLOW       Anywhere             # proxmox gui   
41641/udp                  ALLOW       Anywhere             # from tailscale     
Anywhere on tailscale0     ALLOW       Anywhere                  
4533/tcp                   ALLOW       Anywhere             # navidrome from lan     
8096/tcp                   ALLOW       Anywhere             # jellyfin from lan     
3001/tcp                   ALLOW       Anywhere             # uptime kuma from lan    
8123/tcp                   ALLOW       Anywhere             # home assistant from lan     
445/tcp                    ALLOW       Anywhere                  # NAS from lan
22/tcp (v6)                ALLOW       Anywhere (v6)             
8006/tcp (v6)              ALLOW       Anywhere (v6)             
41641/udp (v6)             ALLOW       Anywhere (v6)             
Anywhere (v6) on tailscale0 ALLOW       Anywhere (v6)             
4533/tcp (v6)              ALLOW       Anywhere (v6)             
8096/tcp (v6)              ALLOW       Anywhere (v6)             
3001/tcp (v6)              ALLOW       Anywhere (v6)             
8123/tcp (v6)              ALLOW       Anywhere (v6)             
445/tcp (v6)               ALLOW       Anywhere (v6)             

Anywhere                   ALLOW OUT   Anywhere on tailscale0       # to tailscale
Anywhere (v6)              ALLOW OUT   Anywhere (v6) on tailscale0  # to tailscale

Anywhere                   ALLOW FWD   Anywhere on vmbr0         
Anywhere on vmbr0          ALLOW FWD   Anywhere on vmbr0         
Anywhere on vmbr0          ALLOW FWD   Anywhere                  
Anywhere (v6)              ALLOW FWD   Anywhere (v6) on vmbr0    
Anywhere (v6) on vmbr0     ALLOW FWD   Anywhere (v6) on vmbr0    
Anywhere (v6) on vmbr0     ALLOW FWD   Anywhere (v6)  

**Node 2:**
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere                  
8006/tcp                   ALLOW       Anywhere                  
Anywhere on tailscale0     ALLOW       Anywhere                  
41641/udp                  ALLOW       Anywhere                  
22/tcp (v6)                ALLOW       Anywhere (v6)             
8006/tcp (v6)              ALLOW       Anywhere (v6)             
Anywhere (v6) on tailscale0 ALLOW       Anywhere (v6)             
41641/udp (v6)             ALLOW       Anywhere (v6)             

Anywhere                   ALLOW OUT   Anywhere on tailscale0    
Anywhere (v6)              ALLOW OUT   Anywhere (v6) on tailscale0

Anywhere                   ALLOW FWD   Anywhere on vmbr0         
Anywhere on vmbr0          ALLOW FWD   Anywhere on vmbr0         
Anywhere on vmbr0          ALLOW FWD   Anywhere                  
Anywhere (v6)              ALLOW FWD   Anywhere (v6) on vmbr0    
Anywhere (v6) on vmbr0     ALLOW FWD   Anywhere (v6) on vmbr0    
Anywhere (v6) on vmbr0     ALLOW FWD   Anywhere (v6) 

# Fail2Ban
**both nodes:**
[proxmox]
enabled = true
port = https,http,8006
filter = proxmox
backend = systemd
maxretry = 5
findtime = 2d
bantime = 1h