def int32_to_ip(int32):
    x = str(bin(int32)[2::])
    if len(x)<32: x = '0'*(32-len(x)) + x
    return f'{int(x[0:8],2)}.{int(x[8:16],2)}.{int(x[16:24],2)}.{int(x[24:32],2)}'

# from ipaddress import IPv4Address

# def int32_to_ip(int32):
#     return str(IPv4Address(int32))


print(int32_to_ip(2149583361))