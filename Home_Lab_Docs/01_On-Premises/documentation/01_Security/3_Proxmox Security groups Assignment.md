# Security Groups ASSIGNMENT
made it into 2 files, because it would ve been to long.

**SECURITY GROUPs ASSIGNMENT:**\
*statefull*\
*order matters(both rules within SG and order of the SGs)*

**node 1, node 2, node 3 and PBS:**\
quorum (not pbs)
proxmox_pbs_gui\
prometheus\
ssh\
ping\
pbs\
loki\
ad_auth\
get_dns\
internet

**ML:**\
prometheus\
ssh\
ping\
loki\
get_dns\
ml_api\
internet

**AD:**\
smb\
ping\
get_dns\
ad_auth\
internet\
rdp

**NAS:**\
smb\
prometheus\
ssh\
ping\
loki\
get_dns\
internet

**Docker:**\
smb\
prometheus\
ssh\
ping\
loki\
get_dns\
applications\
internet

**PDM:**\
proxmox_pbs_gui\
ssh\
ping\
pdm\
ad_auth\
get_dns\
internet


LAST EDIT : 1/10/2026