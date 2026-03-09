made by Chatgpt:
# Stage 1 — Beginner (Functional System)

**Objective:**
Get services working reliably with minimal complexity.

**Typical state:**
	•	Single hypervisor
	•	Services manually configured
	•	No automation
	•	Minimal security controls

**Example stack:**
	•	Proxmox VE
	•	Ubuntu VM or LXC
	•	Jellyfin
	•	Navidrome

**Tasks**
	1.	Install hypervisor
	•	Install Proxmox VE
	•	Configure storage
	•	Create bridge networking
	2.	Create service containers or VMs
	•	Ubuntu VM or LXC containers
	•	Install applications
	3.	Manual service configuration
	•	Ports
	•	storage directories
	•	service users
	4.	Basic networking
	•	internal IP addresses
	•	router NAT or VPN access
	5.	Manual updates

**Outcome**
You now have a working system, but it has weaknesses:
	•	no backup protection
	•	no monitoring
	•	limited security isolation
