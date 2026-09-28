from pathlib import Path
from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser(description = "DryRun or DELETE FILES in PATH older than DAYS")
parser.add_argument("path" , nargs = "?", default = "/var/log", help = "Path to look for old files")
parser.add_argument("--days", "-d",type = int, nargs = "?", default = 30, help = " modification time older than DAYS" )
parser.add_argument("--force", "-f", action = "store_true", help = "ONLY IF YOU ARE SURE")
args = parser.parse_args()

path = Path(args.path)
days = args.days
force = args.force

def files_to_delete():
    files = []
    f = {}
    now = datetime.now()
    if path.exists() == False:
        print("Dir does not exists")
        return f
    try: 
        for file in path.rglob("*"):
            mtime = datetime.fromtimestamp(file.stat().st_mtime)
            age = now - mtime
            if age > timedelta(days = days):
                f = {"path" : file, "mtime" : age}
                files.append(f)
        return files
    except FileNotFoundError:
        print("File not Found")

def delete(files):
    for file in files: 
        path = Path(file["path"])
        print(f"DELETING : {path}")
        path.unlink()

def total_storage(files):
    total = 0
    for file in files: 
        path = Path(file["path"])
        total += path.stat().st_size
    return round(total / 1024 ** 2, 2)

files = files_to_delete()
print("DRYRUN:")
for file in files:
    print(f"FILE : {file["path"]}")
if force is True:
    print(f"{(total_storage(files))}MB FREED")
    print(f"{len(files)} DELETED")
    answer = input("Are you sure?[y,N]")
    if answer == "y":
        delete(files)
    else:
        print("Aborting")
else:
    print(f"{(total_storage(files))}MB would be freed")
    print(f"{len(files)} would be deleted")
    print("Run with --force or -f to delete files")
    