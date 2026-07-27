# PFSENSE SETUP 

**prereq:**
bough a smart switch, created VLAN: 10,100,999: (using 802.1Q VLAN)
port 1: VLAN 1000 (WAN)                                            PVID: 100
port 2: VLAN 10 20                                                 PVID: 20
port 3: VLAN 10 20 trunk vlan 10 and 20                            PVID: 20
port 4: VLAN 10 20                                                 PVID: 20
port 5: VLAN 10 20                                                 PVID: 20
port 6: VLAN 10 20                                                 PVID: 20
port 7: VLAN 10 20                                                 PVID: 20
port 8: VLAN 10 100(WAN) 20 trunk vlan 10, 20 and  100                     PVID: 20

**step 1:**
For now I've disconnected all 3 devices ( 2 nodes and my personal laptop) from internet and connected them to the switch via ethernet, *temporaly* on respectively port 3,4,5 ( all VLAN 10). 
*temporaly* created a static routing rule to foward 10.10.10.0/24 traffic to 192.168.1.37(node 1) and 10.20.20.0/24 to 192.168.1.38(node 2)
to access music and pfsense VM to configure it properly.  (sudo route -n 10.10.10.0 192.168.1.37) or directly (sudo route -n add -net 10.10.10.0/24 -interface en9) used this command instead of the previous one because if I have both wifi and ethernet connected to the mac, the default gateway of the mac is the home router, but i need it to be the switch to access the nodes. 
*Reminder* remove the static routing rule once pfsense is configured: sudo route delete 10.10.10.0

for now commands run on mac: 
sudo route -n add -net 192.168.1.37 -interface en9
sudo route -n add -net 192.168.1.38 -interface en9
sudo route -n add 10.10.10.0/24 192.168.1.37
sudo route -n add 10.20.20.0/24 192.168.1.38    


**step 2:**
changed all the ips corrispectively:
node1: host = 192.168.20.1/24 VMs/LXC = 192.168.10.x/24
node2: host = 192.168.20.2/24 VMs/LXC = 192.168.10.x/24
pfsense: nic0(LAN20) = 192.168.20.3(should've done x.x.x.1 but well) nic1(WAN)= 192.168.1.55 nic2(LAN10)=192.168.10.1
connected back everything

**step 3:**
setup pfsense with the right interfaces with the right vlan tags, 1000 for WAN, 20 for Management, 10 for servers. 
created NAT rules to allow traffic to flow between LANs and WANs, now every host and VMs/LXCs has access to each other and the internet by using the NAT (in the future I will make it more secure)
typical traffic flow: 
* 192.168.10.3:4533(navidrome) --> 192.168.10.1(pfsense) ---> 192.168.20.1(node1_host)  
* 192.168.1.139(my laptop) ---> 192.168.1.1(ISP's router) ---> 192.168.1.55(pfsense) ----> 192.168.20.1(node1_host)

**result** 
Now everypacked that has to access internet or computers outside it's own VLAN or another computer has to passthough the pfsense VM, centralizing packet management into pfsense for future projects with packet monitoring/DNHC/DNS servers/filtering.
The result is visible in the network schema that I'm gonna do later