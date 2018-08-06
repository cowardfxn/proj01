# Enable IPv4 forwarding on Linux

## Enable IP Forwarding on the fly

`$ sysctl -w net.ipv4.ip_forward=1`

Or

```
$ sudo chmod 644 /proc/sys/net/ipv4/ip_forward
$ sudo echo 1 > /proc/sys/net/ipv4/ip_forward
```

## Permanent setting using /etc/sysctl.conf

 1. Add the following to file /etc/sysctl.conf:  
    `net.ipv4.ip_forward = 1`
 2. When file is saved, enable the changes made in sysctl.conf file
    `sysctl -p /etc/sysctl.conf`
 3. Restart the network service  
  On RedHat based systems:  
    `service network restart`  
  On Debian/Ubuntu systems:  
    `/etc/init.d/procps.sh restart`
