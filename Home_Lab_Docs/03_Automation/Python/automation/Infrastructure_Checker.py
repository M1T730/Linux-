import yaml
from pathlib import Path
import logging
import subprocess
from logging.handlers import RotatingFileHandler
import ipaddress


LOG_DIR = Path("/var/log/homelab-checker")
LOG_FILE = LOG_DIR / "checker.log"
LOG_DIR.mkdir(parents=True, exist_ok=True)
hosts = Path("/home/matteo/hosts.yml")

handler = RotatingFileHandler(
    LOG_FILE,
    backupCount = 3
)

logging.basicConfig(
    handlers = [handler],
    format = " %(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level = logging.DEBUG
)
hostname = subprocess.run(["hostname"], capture_output= True, text = True)
logger = logging.getLogger(hostname.stdout)

def ping(ip):
    try: 
        result = subprocess.run(["ping", "-c", "2", ip], capture_output= True, text = True, timeout = 4)
        lines = result.stdout.splitlines()
        if result.returncode == 0:
                logger.info(f"Ping to {ip} Successfull with latency: {lines[-1]}")
                return True
        else:
            return False
    except subprocess.TimeoutExpired:
         logger.warning(f"Ping to {ip} took longer than 4 secs, probably failed")
  
def check_internet():
    logger.debug("Internet:")
    if ping("8.8.8.8") is False:
         logger.warning("\n Ping to 8.8.8.8 Failed")
    
    if ping("google.com") is False:
         logger.warning("\n Ping to google.com Failed")

def check_intranet(hosts, name = "idk"):
    logger.debug(f"INTRANET: {name}")
    failed = []
    for host in hosts: 
        if ping(host) is False:
            failed.append(host)
    if len(failed) > 0:
         logger.warning(f" \n THESE NODES FAILED: {failed}")

def check_ip(ip):
    try:
        if ipaddress.ip_address(ip):
            return (ip)
    except ValueError:
        logger.warning(" Invalid IP ")
        return ("8.8.8.8")
    
logger.debug("Starting CHECKER")
check_internet()
try:
    with hosts.open() as file:
        data = yaml.safe_load(file)
    nodes = []
    servers = []

    for node in data["hosts"]["nodes"]:
        ip = check_ip(node(["ip"]))
        nodes.append(ip)
        nodes.append(node["hostname"]+".lab.internal")

    for srv in data["hosts"]["servers"]:
        servers.append(srv["ip"])
        servers.append(srv["hostname"]+".lab.internal")   

    check_intranet(nodes, "nodes")
    check_intranet(servers, "servers")

except FileNotFoundError:
    logger.warning("No hosts file")
finally:
    logger.debug("CHECKER CLOSED")

