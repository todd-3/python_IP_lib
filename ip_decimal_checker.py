from typing import Callable

__version__ = '0.3.1'

def ip_to_int(addr: str) -> int:
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
    base_ip, cidr = ip_to_int(split_elements[0]), cidr_to_wildcard_int(int(split_elements[1]))

    return base_ip, base_ip + cidr

def check_ip_contains(addr: str, ip_range: str) -> bool:
    ip = ip_to_int(addr)
    cidr_range = cidr_to_int_range(ip_range)
    return cidr_range[0] <= ip <= cidr_range[1]

def int_to_ip(addr: int) -> str:
    """Converts an integer IP address to its dotted decimal form"""
    binary_form = bin(addr)[2:].zfill(32)  # get binary 1s and 0s of addr int and leftpad to 32 characters
    octets = [str(int(binary_form[i: i+8], 2)) for i in (0, 8, 16, 24)]
    return ".".join(octets)

def set_cidr_checker(cidr: str) -> Callable[[str], bool]:
    """Creates a lambda function to check if an IP address falls within the CIDR range provided to this function"""
    ranges = cidr_to_int_range(cidr)
    return lambda addr: ranges[0] <= ip_to_int(addr) <= ranges[1]


if __name__ == "__main__":
    print(int_to_ip(3232235520))
