# Smart Switch Setup

**prereq:**
bought a smart switch, created VLAN: 10,100,1000: (using 802.1Q VLAN)
VLAN 1: DEFAULT  VLAN 10: SERVERS VLAN 20: MANAGEMENT  VLAN 1000: WAN

port 1: access VLAN 1000                                             
port 2: trunk VLAN 10, 20                                      native: 999      
port 3: trunk VLAN 10, 20                                      native: 999     
port 4: access VLAN 20                                               
port 5: access VLAN 20                                                
port 6: access VLAN 20                                                
port 7: access VLAN 20                                                
port 8: trunk VLAN 10, 20, 1000                                native: 999      

