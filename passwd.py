# nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false

for line in open("/etc/passwd", "r"):
    if line.startswith("#"):
        continue
    
    user, _ , uid, gid, name, homedir, shell = line.split(":")
    print user, name
