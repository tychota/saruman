# Modules externes
from plumbum import local

modprobe = local["modprobe"]
lsmod = local["lsmod"]
