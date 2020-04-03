import os
cmd = "secrets workload buckets pie admin-server.radar-radar-admin-server.radar-uat | awk 'NR == 2 {print $1}'"
os.system(cmd)
