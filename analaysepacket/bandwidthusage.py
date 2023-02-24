import psutil
import matplotlib.pyplot as plt
interface="eth0"
net_io_counters=psutil.net_io_counters()
print(net_io_counters)
bytes_received=net_io_counters.bytes_recv / 1024 / 1024
bytes_sent=net_io_counters.bytes_sent / 1024 / 1024
plt.bar(["Received","Sent"],[bytes_received,bytes_sent])
plt.ylabel("Bandwidth usage (MB)")
plt.title("Network usage for interface {}".format(interface))
plt.show()