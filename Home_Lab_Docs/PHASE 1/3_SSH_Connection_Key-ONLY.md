# SSH_Connection_Key-ONLY

**step 1**
install ssh on ubuntu server: 
```bash
sudo apt update
sudo apt install openssh-server
```

**step 2**
generate ssh keys on client machine, via:
```bash
ssh-keygen -t ed25519
```

**step 3**
copy public to the target server via:
```bash
ssh-copy-id -i path_to_public_key user@server_ip
```

**step 4** 
disable ssh connection via password modifying */etc/ssh/ssh.config* , setting *no* to *PasswordAuthentication*
restart to apply changes: 
sudo systemctl restart sshd

**step 5** (optional)
creating envs for username and server_ip in client, 
```bash
vim ~/.bashrc*
export env_name=username@server_ip
```

**update_afterstage5**
resetted to ssh to proxmox and in Linux VM