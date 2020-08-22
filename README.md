# Packet_Filtering_Firewall
Detect and Drop Unwanted IP Addresses coming to your Network

Can only usable at Linux Systems.

You have to use one command to change some Linux IP Tables Rules.
Command :- iptables -I FORWARD -j NFQUEUE --queue-num 0 (It is only applied when you want to filter forwarded trafic.)

If you want to apply firewall for your system then use below command.
command :- iptables -I OUTPUT -j NFQUEUE --queue-num 0 && iptables -I INPUT -j NFQUEUE --queue-num 0

There is one more modification in script.
You have to add your list of IP's in to script.
According to your list, script will perform the filteration.

Now, you are ready to go

Just go and run the script.

