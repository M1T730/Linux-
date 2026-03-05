# SSH_Connection_Key-ONLY

**step 1**
install ssh on ubuntu server: 
*sudo apt update*
*sudo apt install openssh-server*

**step 2**
generate ssh keys on client machine, via *ssh-keygen -t ed25519*

**step 3**
copy public to the target server via *ssh-copy-id -i path_to_public_key user@server_ip* 

**step 4** 
disable ssh connection via password modifying */etc/ssh/ssh.config* , setting *no* to *PasswordAuthentication*

**step 5** (optional)
creating envs for username and server_ip in client, *vim ~/.bashrc*