import netfilterqueue
import scapy.all as scapy

# ip_list = ['157.240.220.35', '69.171.250.35', '157.240.0.35', '157.240.14.35', '69.171.250.35', '31.13.80.36', '157.240.14.35', '185.60.219.35', '31.13.64.35', '179.60.192.36', '31.13.83.36', '157.240.17.35', '31.13.84.36', '157.240.18.35', '157.240.200.35', '157.240.14.35', '31.13.89.35', '157.240.222.35', '179.60.194.35', '31.13.71.36', '157.240.7.35', '31.13.70.36', '31.13.70.36', '69.171.250.35', '157.240.16.35', '157.240.7.35', '31.13.66.35', '31.13.79.35', '37.68.0.1/16', '31.13.79.7', '157.240.198.35']
ip_list = List_of_ip_address

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	# print(scapy_packet.show())
	# packet.accept()
	for i in ip_list:
		if scapy_packet[scapy.IP].dst == i:
			print("unwanted request detected")
			packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()