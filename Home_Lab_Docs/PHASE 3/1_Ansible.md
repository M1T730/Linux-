# Ansible configuration and utilization:

using Ansible from now on to IaC the homelab and to automate tasks + execute tasks on multiple vms withough going though 1 by 1.

**step 1:**
Installed Ansible in my macbook, that has ssh access to every important vm and lxc.

**step 2:**
to avoid the hassle of putting the password everytime, I did sudo visudo to make so that my users I'm SSHing can sudo command withough password.
matteo ALL=(ALL) NOPASSWD: ALL

(future vms I will automatically set them up)

**step 3:** 
First I tested the Ansible playbook with update and upgrade:
```yaml
- name: Apt update and apt upgrade
  hosts: all
  become: yes

  tasks:

  - name: Update and upgrade apt packages
    apt:
      upgrade: yes
      update_cache: yes
      cache_valid_time: 86400
```

**step 4:** 
Set Up Node_Exporter and PromTrail service in each VMs I wanted to Monitor and Centralized Logging respectively:

node_exporter.yml:
```yaml
- name: Install Node Exporter and Promtail
  hosts: all
  become: yes

  tasks:

  - name: Download Node Exporter
    get_url:
      url: https://github.com/prometheus/node_exporter/releases/download/v1.10.2/node_exporter-1.10.2.linux-amd64.tar.gz
      dest: /tmp/node_exporter.tar.gz

  - name: Extract Node Exporter
    unarchive:
      src: /tmp/node_exporter.tar.gz
      dest: /tmp
      remote_src: yes

  - name: Install Node Exporter binary
    shell: |
      cp /tmp/node_exporter-*/node_exporter /usr/local/bin/
      chmod +x /usr/local/bin/node_exporter

  - name: Create node_exporter user
    user:
      name: node_exporter
      shell: /bin/false
      system: yes

  - name: Create Node Exporter service
    copy:
      dest: /etc/systemd/system/node_exporter.service
      content: |
        [Unit]
        Description=Node Exporter
        After=network.target

        [Service]
        User=node_exporter
        ExecStart=/usr/local/bin/node_exporter

        [Install]
        WantedBy=multi-user.target

  - name: Enable and start Node Exporter
    systemd:
      name: node_exporter
      enabled: yes
      state: started
```
promtrail.yml:

```yaml
- name: Install Promtail with journald support
  hosts: all
  become: yes

  vars:
    loki_url: "http://192.168.10.130:3100/loki/api/v1/push"
    promtail_version: "latest"

  tasks:

  - name: Create promtail user
    user:
      name: promtail
      system: yes
      shell: /usr/sbin/nologin
      create_home: no

  - name: Add promtail to systemd-journal group
    user:
      name: promtail
      groups: systemd-journal
      append: yes

  - name: Create promtail directories
    file:
      path: "{{ item }}"
      state: directory
      owner: promtail
      group: promtail
      mode: '0755'
    loop:
      - /var/lib/promtail
      - /etc/promtail

  - name: Download Promtail
    get_url:
      url: https://github.com/grafana/loki/releases/download/v3.6.0/promtail-linux-amd64.zip
      dest: /tmp/promtail.zip

  - name: Extract Promtail
    unarchive:
      src: /tmp/promtail.zip
      dest: /tmp
      remote_src: yes

  - name: Find Promtail binary
    find:
      paths: /tmp
      patterns: "promtail-linux-amd64*"
    register: promtail_bin

  - name: Install Promtail binary
    copy:
      src: "{{ promtail_bin.files[0].path }}"
      dest: /usr/local/bin/promtail
      mode: '0755'
      remote_src: yes
  
  - name: Create Promtail config
    copy:
      dest: /etc/promtail/promtail.yml
      owner: root
      group: root
      mode: '0644'
      content: |
        server:
          http_listen_port: 9080

        clients:
          - url: {{ loki_url }}

        positions:
          filename: /var/lib/promtail/positions.yaml

        scrape_configs:
          - job_name: systemd-journal
            journal:
              max_age: 12h
              labels:
                job: systemd-journal
                host: {{ inventory_hostname }}

            relabel_configs:
              - source_labels: ['__journal__systemd_unit']
                target_label: unit

              - source_labels: ['__journal__hostname']
                target_label: host

  - name: Create systemd service for Promtail
    copy:
      dest: /etc/systemd/system/promtail.service
      content: |
        [Unit]
        Description=Promtail
        After=network.target

        [Service]
        User=promtail
        Group=systemd-journal
        ExecStart=/usr/local/bin/promtail -config.file=/etc/promtail/promtail.yml
        Restart=always

        [Install]
        WantedBy=multi-user.target

  - name: Set permissions for promtail state directory
    file:
      path: /var/lib/promtail
      state: directory
      owner: promtail
      group: promtail
      mode: '0755'

  - name: Reload systemd
    systemd:
      daemon_reload: yes

  - name: Enable and start Promtail
    systemd:
      name: promtail
      enabled: yes
      state: started
```