# Create and Run Navidrome and Jellyfish on Docker as containers

**Prerequisites:**
having docker and docker compose 

v1: just run Navidrome
v2: running Navidrome and Jellyfish as media server, both share the samba share

**step 1:** 
creating media stack as the common directory and creating 1 directory for each application
```bash
mkdir -p ~/media-stack/jellyfin
mkdir -p ~/media-stack/navidrome
```

**step 2:**
```bash
vim docker-compose.yml
```
```yaml
services:
  navidrome:
    image: deluan/navidrome:latest
    user: 1000:1000
    ports:
      - "4533:4533"
    restart: unless-stopped
    volumes:
      - "./navidrome:/data"          # Navidrome settings stay here 
      - "/mnt/nas_music:/music:ro"    # Points to the NAS

  jellyfin:
    image: jellyfin/jellyfin:latest
    user: 1000:1000
    ports:
      - "8096:8096"
    restart: unless-stopped
    volumes:
      - "./jellyfin:/config"         # Jellyfin settings stay here 
      - "/mnt/nas_music:/data/music:ro" # Points to the SAME NAS folder
```

**Verification:**
```bash
docker compose up -d 
docker compose ls
```