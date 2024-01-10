# IP Lib
This project is a small experiment for me to learn more about how IP addresses and cidr/netmasks work

It provides several methods
 - ip_to_int(str) -> int: takes in an ip address string (eg - '192.168.50.200') and returns its integer value (eg - 3232248520)
 - cidr_to_wildcard_int(int) -> int: takes in a cidr range (eg: 24) and returns its wildcard value as an int (eg - 255)
 - cidr_to_netmask_int(int) -> int: takes in a cidr range (eg: 24) and returns its netmask value as an int (eg - 4294967040)
 - cidr_to_int_range(str) -> (int, int): takes in an ip address with cidr range (eg - '192.168.0.0/16') and returns a tuple with its minimum and maximum ip as ints (eg - (3232235520, 3232301055) )
 - check_ip_contains(str, str) -> bool: takes an ip address and ip with cidr (eg - '192.168.23.25', '192.168.23.0/24') and returns a bool value for wether the ip address falls within the cidr range
 - int_to_ip(int) -> str: takes an integer ip value (eg - 3232241428) and returns it as its traditional string form (eg - '192.168.23.20')
 - set_cidr_checker(str) -> lambda: takes in an ip with cidr range and returns a lambda expression to check if a provided ip address is within that range
