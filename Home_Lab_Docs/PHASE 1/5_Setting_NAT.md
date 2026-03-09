# Setting up Networking for Containers and VMs (NAT/Routed Setup)

**Prerequisites:**
1. install and run Proxmox(like installing Ubuntu Doc N.1)
2. setup ethernet connection to proxmox host (bridge: vmbr0)

**step 1:**
Edit the file */etc/network/interfaces* on the *Proxmox Host*:
add an bridge to act as NAT, routing traffic to vmbr0, so ISP's router only sees traffic with Proxmox's Mac Adrr. , avoiding port security issues: 

```bash
auto vmbr1
iface vmbr1 inet static
        address 10.10.10.1/24
        bridge-ports none
        bridge-stp off
        bridge-fd 0
        # Enable Packet Forwarding and Masquerading (NAT) on boot
        post-up echo 1 > /proc/sys/net/ipv4/ip_forward
        post-up iptables -t nat -A POSTROUTING -s '10.10.10.0/24' -o vmbr0 -j MASQUERADE
        post-down iptables -t nat -D POSTROUTING -s '10.10.10.0/24' -o vmbr0 -j MASQUERADE
```

*Apply changes with: `ifreload -a` or `reboot`.*

**step 2**
When creating or modifying LXC container or VM set network parameters: 

*Bridge: `vmbr1`*
*IPv4/CIDR: `10.10.10.#/24` 
*Gateway (IPv4): `10.10.10.1` (The IP assigned to vmbr1 above)*

**step 3:**
everything on top of Proxmox is in a private network now, to see it from our LAN(`192.168.1.#`) we need modify router settings, adding Static Route:

address: `10.10.10.#` (LXC's IP)
subnet:  `255.255.255.0/24`
gateway: `192.168.1.#` (Proxmox's IP)

Router now knows that the traffic for `10.10.10.#` has to be sent to Proxmox's IP
*Why you need this?* because router does not allow multiple MAC addresses on the same LAN port, so we bypass it making our Proxmox host become a router, to create a NAT

**Verification:**
*Check Gateway: `ping 10.10.10.1`*
*Check Internet: `ping  8.8.8.8`*
*Check DNS: `ping google.com`*