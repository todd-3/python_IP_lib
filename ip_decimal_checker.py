def ip_to_decimal(addr: str) -> int:
    """Converts an IP address from its dotted decimal format to a 32-bit integer form"""
    octets = addr.split(".")  # split ip address into its 4 octets
    decimals = [int(octet) << 8 * (3-num) for num, octet in enumerate(octets)]  # bitshift each octet by a multiple of 8
    return sum(decimals)  # sum bit-shifted octets together for final decimal value

def cidr_to_wildcard_int(cidr: int) -> int:
    """Calculates the integer wildcard value for a cidr"""
    mask_value = 32 - cidr
    return (2 ** mask_value) - 1

def cidr_to_netmask_int(cidr: int) -> int:
    """Calculates the integer netmask for a cidr"""
    return 0xffffffff - cidr_to_wildcard_int(cidr)

def cidr_to_int_range(addr: str) -> tuple[int, int]:
    """Calculates the upper and lower ip addresses of a given cidr range, ip address are returned as integers"""
    split_elements = addr.split("/")
    base_ip, cidr = ip_to_decimal(split_elements[0]), cidr_to_wildcard_int(int(split_elements[1]))

    return base_ip, base_ip + cidr

def check_ip_contains(addr: str, ip_range: str) -> bool:
    ip = ip_to_decimal(addr)
    cidr_range = cidr_to_int_range(ip_range)
    return cidr_range[0] <= ip <= cidr_range[1]

if __name__ == "__main__":
    print(check_ip_contains("192.168.51.154", "192.168.50.0/24"))
