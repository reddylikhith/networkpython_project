from scapy.all import *
packets=sniff(filter="ip and tcp",count=100)
wrpcap=("captured_packets.pcap",packets)